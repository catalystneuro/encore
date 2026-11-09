**A. Outcomes**

The claims file has 36 claims. Outcomes marked * come from the CCG notebook, which has the jitter bug in B1. Treat them as provisional until it is rerun.

| Claim | Outcome | Reason |
|---|---|---|
| methods-sessions-passing-qc | reproduced | 58 sessions; wt 30, Pvalb 8, Sst 12, Vip 8 (cell 12). |
| methods-probes-ccf | reproduced | 332 probes, 284 mapped (cell 14). |
| ed1jk-units-per-experiment | reproduced | 686.2 ± 144.6 per experiment, 128.8 per probe, 56.2 per area, 6.07 areas. All within tolerance (cell 16). |
| fig1g-receptive-fields | partially_reproduced | Visual areas 60.8% (within). Hippocampus 1.61% pooled and 1.74% as the mean over mice; both are outside 1.4 ± 0.14% (cell 18). |
| fig2-sharp-peak-pairs | reproduced* | With the 2 s window and all units: 17,592 peaks, 2,116,259 pairs, 0.94% per mouse. All within tolerance. 26 mice were used, not 25. |
| fig2d-v1-leads-lm-example | reproduced* | 4 mice have a median of 4.0 ms with p < 0.05 and V1-LM higher (CCG cell 9). |
| fig2-neighbour-offsets-across-mice | partially_reproduced* | Under 2 s with all units, 4 of 5 pairs agree; AL-PM gives p = 1.8e-5. Only the ED1j-filter reading gives 5 of 5 (AL-PM p = 0.057, 4 mice), and that reading fails the parent claim's counts (4,850 peaks). |
| ed7c-v1-leads-am-follows | partially_reproduced* | 9 of 10 pairs: PM→AM is −1.54 ms. Only the 3 s + ED1j reading gives 10 of 10, and that reading fails the parent claim's counts. |
| fig2f-directionality-vs-anatomy | reproduced* | r = 0.809, p = 1e-5. This is near the upper tolerance edge of 0.814; the 3 s reading gives 0.825, outside it. The paper's precomputed matrix gives 0.735. |
| ed7e-distance-does-not-explain | blocked (metadata_insufficient) | Electrode y equals z in all 58 session files (cell 9 of the main notebook), so the left-right coordinate is missing. The probe files were not checked (see D). |
| ed7fg-absent-in-spontaneous | not_reproduced* | The correlation in spontaneous activity is significant under every reading: r = 0.50 to 0.60, p = 0.004 to 0.022 with DS averaged across mice. |
| ed8-total-hierarchy-score | reproduced* | THS = 0.904, which lies between 0.15 and 1.54. |
| fig3c-latency-hierarchy | reproduced | All flashes, 250 ms window: r = 0.959, p = 0.0002 (cell 24). |
| ed9a-latency-pairs | partially_reproduced | One pair disagrees: RL-AL is not significant (cell 27). |
| fig3f-rf-size-hierarchy | reproduced | r = 0.958, p = 1.9e-4 (cell 29). |
| ed9d-rf-size-pairs | partially_reproduced | Two pairs disagree: LM-AL and RL-AL (cell 31). |
| fig3i-modulation-index-hierarchy | reproduced | r = −0.954, p = 2.4e-4, and LGN has the highest mean (cell 33). |
| ed9e-modulation-index-pairs | not_reproduced | Four pairs disagree: LM-LP, LM-RL, RL-LP and RL-AL (cell 35). |
| ed9fg-intrinsic-timescale-not-correlated | reproduced | r = −0.16, p = 0.71; the code variant gives p = 0.49 (cell 37). See B6. |
| fig3l-response-decay-timescale-hierarchy | reproduced | 0 to 250 ms window: r = 0.804 (tolerance 0.774 to 0.946), p = 0.016 (cell 39). |
| ed9h-response-decay-pairs | not_reproduced | Four pairs disagree: LGN-AL, LGN-LM, LM-AL and RL-LP (cell 41). |
| fig3-unit-counts | not_reproduced | Under the claims' latency procedure: 13,347 or 24,481 units against 15,713 ± 1,571, and 5,842 against 7,837 ± 784 (cell 43). The code's 200 ms window (17,167 and 8,381) and the paper's tables both land within tolerance, but those are not the claims' reading. |
| ed9bc-spontaneous-latency | reproduced | Against hierarchy p = 0.49. Against baseline rate r = −0.991 and −0.987, both within tolerance (cell 45). |
| ed9ij-firing-rate-not-correlated | reproduced | Mean of log10 rate: r = −0.33, p = 0.43 (cell 47). |
| ed10b-layers | not_reproduced | All four differences have the right sign and p < 0.05, but only the RF area (105 deg²) is within tolerance. Latency 1.33 ms (expected 2.59 ± 0.26), log10 MI 0.117 (0.09 ± 0.009), decay 7.71 ms (6.6 ± 0.66). One part out of four is below the two needed for partial (cell 49). |
| ed10ce-superficial-lead-deep | reproduced* | Superficial-to-deep DS is 0.25 to 0.37 under every reading. This is the claim most exposed to B1. |
| anatomical-hierarchy-order | reproduced | The order of the code's scores matches; the bootstrap test was not run (cell 51). |
| fig4b-behaviour-performance | blocked (data_missing) | No deposit is named. 000253 is passive. 000713 (Visual Behavior Neuropixels, 81 subjects) is a later, different release. |
| fig4e-behaviour-latency-hierarchy | reproduced | r = 0.917, p = 0.0013. |
| fig4f-change-modulation-hierarchy | reproduced | r = 0.828, p = 0.011. All eight areas are above 0, and active exceeds passive in 8 of 8 areas. |
| ed9k-cmi-hit-not-miss | reproduced | Hit r = 0.853, p = 0.007; miss p = 0.197. |
| ed9lmn-other-responses-not-correlated | reproduced | Active-state p values are 0.13, 0.57 and 0.80. |
| fig4h-decoder-behaviour-hierarchy | reproduced | r = 0.881, p = 0.004; the LGN mean is −0.015 ± 0.032, so its interval includes zero. |
| ed9p-decoders-above-chance | reproduced | All 8 areas are above the chance level of 0.5 under both readings; accuracy against hierarchy p = 0.14. |
| link-unit-tables | partially_reproduced | 100% of ids match and the timescales agree at 99.3% and 99.6%. The time to first spike agrees within 1 ms for only 16% of units (cell 20). |
| methods-gaze-stability | reproduced | Filtered, radial: 6.59 ± 2.18 degrees with a maximum of 14.29, both within tolerance, over 50 mice. |

**B. Problems**

1. [affects a conclusion] `siegle.ccg_group` uses the wrong jitter expectation at negative lags. For k < 0 it computes `G[k]` as `W[:, :LW+k] @ W[:, -k:].T`, which equals `G[|k|]`; it should be `G[|k|].T`.
   - I checked this against an exact brute-force computation on synthetic trains. Positive lags match exactly. Negative lags are off, for example −0.032 against −0.015 at −10 ms and −0.08 against 0.001 at −50 ms.
   - The error moves each pair's CCG toward a positive lag for whichever unit's rate rises first. So it biases peak offsets toward the latency order, which tracks the hierarchy and the superficial-before-deep order (ed10b).
   - It also adds a ramp to the negative flank, which inflates the flank SD and changes the peak counts.
   - Every CCG claim depends on this, and the bias favours fig2d, the neighbour-offset claim, ed7c, fig2f, ed8 and ed10ce.
2. [affects a conclusion] CCG `peak_table` adds every within-area pair twice, once with its offset and once with the offset negated. The V1-V1 (and other within-area) reference samples in `per_mouse_test` are therefore duplicated and mirrored, which overstates the rank-sum and Fisher significance. This bears on AL-PM in fig2-neighbour-offsets-across-mice.
3. [affects a conclusion] The CCG notebook (cells 9, 11 and 13) counts dependent claims as reproduced under readings (ED1j filter, 3 s window) whose own peak and pair counts fail fig2-sharp-peak-pairs. The readings should be held consistent across the parent claim and the claims that depend on it.
4. [affects a conclusion] `siegle.first_spike` with a 200 ms window is described as the procedure of get_flash_PSTH.py, yet it matches the paper's table within 1 ms for only 16% of units (median difference 4 ms, 95th percentile 37 ms). No cause is found. The latency cut sets the unit counts used in fig3-unit-counts, ed10b and every Figure 3 selection.
5. [does not affect a conclusion] The CCG analysis uses 26 mice where the paper uses 25. This is stated as an assumption.
6. [does not affect a conclusion] `intrinsic_timescale`: the median fitted timescale over all units is 1.0002 ms, the lower bound (cell 9). Most fits are degenerate under the Methods reading, so the absence result in ed9fg is a weak test. The code variant agrees with it.
7. [does not affect a conclusion] `decay_timescale` builds its time axis as `linspace(0, nb/2*10, ...)`, a step of 10.42 ms where the bins are 10 ms. This follows the code, which reproduces the paper's table at 99.3%.
8. [does not affect a conclusion] fig1g counts units with no Gabor spikes (p = NaN) as not significant. Dropping them gives 64.1% and 1.71%, which leaves both judgements unchanged.

Claims-file note: in ed10b, "0.09 MI difference" is fixed as log10 MI from the code. The paper's text says "MI", and the raw-MI variant that the claims file lists was not run.

**C. What I could not check, and the output that would settle it**

- The CCG results with B1 fixed: a rerun of the CCG notebook with `G[-m] = G[m].T`.
- The within-area reference with each pair counted once (B2): the Fisher table rerun that way.
- Why the latency disagrees with the paper's table (B4): a per-unit comparison for a few units, with each trial's first-spike time.
- Whether the AllenSDK `p_value_rf` uses spike counts or a binary response: the paper's code is not in the materials.
- How many units in `it_sel` sit at the 1 ms bound.
- The raw-MI difference for ed10b.
- The probe-session match across the 25 CCG mice versus the 26 used.

**D. Blocked claims, checked against the archive**

- ed7e: 000022 holds 143 probe LFP files, each with its own electrodes table. The notebook checked only the session files, so the left-right coordinate may be present in the probe files. A 2D (AP and DV) distance could also be run as a partial test.
- fig4b: no dandiset holds the paper's 21 behaviour sessions. The 000253 metadata lists optogenetic and electrophysiological approaches, with no behaviour. 000713 is a separate, later Visual Behavior Neuropixels release with 81 subjects. Nothing can be tested.
