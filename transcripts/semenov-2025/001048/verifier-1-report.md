**Verifier report, round 1: Semenov et al. 2025 (doi:10.1016/j.xcrp.2025.102660)**

Two mismatches come first, because they affect everything below.

- **Wrong claims file version.** The notebook was written against a different claims file. Its claim ids (`ap-selection`, `fig1-20khz-needs-twice-the-field`, `fig2d-5ap-above-1ap`, `fig3-not-heating`, `fig4-orientation-and-poles`, `fig5-sine-asymmetry`, `fig6-sine-less-than-pulse`, …) and its readings O1–O6 are not the ones in the claims file I was given. That file has 26 claims, with readings O1–O4: strobe ROIs, LOESS, form of the regression, and identity of cells C7/C8.
- **Dataset mismatch.** The claims file says it is for dataset 001274; the attempt targets 001048. The archive confirms 001048 is a HEK-cell TIRF study that only lists this paper as a related resource. The notebook's statement that "the claims file marks every claim `data: elsewhere`" is false for this file: the Figure 5, 6 and S3 claims are in-dataset (001274).

I judged each claim of the given file from the notebook outputs that bear on it.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1-pure-sine-excites-all | blocked (methods_underspecified) | ROI c, cell 17: 2 kHz 96.4% (27/28); 20 kHz 88.2% under the notebook's AP reading (a) but 94.1% under (b). The readings disagree, which the criterion says blocks the claim. The claims file's own reading (b), a rise of 5% within 5 ms, was never run. |
| fig1-onset-delay | not_reproduced | Median first-AP latency at the near-threshold session is 66–67 ms for ROI c under all readings (cell 17), outside 90–220 ms; 54 ms at 2 kHz (cell 18). The Spearman part passes (40/40 negative). |
| fig1-max-rate-ceiling | not_reproduced | Median ceiling is 40–44 Hz for ROI c and 28–44 Hz across all readings (cell 17), outside 54–99 Hz. |
| fig1-excitation-block | not_reproduced | Applying the claims criterion to cell 21: at most 4 of 32 neurons have a mean dF above 5% in the last 100 ms at their highest voltage. The notebook's own test (cell 20) finds 0–2. |
| fig2d-20khz-twofold-threshold | blocked (metadata_insufficient) | The files give nominal voltages and say "calibration factors are frequency-dependent and will be reported separately"; I confirmed this via the API. So the 20/2 kHz field ratio cannot be formed. Taken at face value, the voltage ratios are 2.27–2.86 for ROI c, outside 2±0.2, although every p < 1e-4 (cell 25). |
| fig2d-modulated-thresholds-higher | partially_reproduced | ROI c: 2 of 3 pairs significant and higher under AP reading (a) (20k 1-AP p=0.021, 20k 5-AP p=0.031); 1 of 3 under (b). The 2-kHz 5-AP pair has p=0.09. The 20-kHz modulated group has only 3 neurons (cell 30). |
| threshold-2khz-unmodulated | blocked (metadata_insufficient) | The nominal conversion gives 75.6 V/cm (amplitude reading) or 151 V/cm (peak-to-peak), against 57.7±3.6 (cell 30). The files say the true amplitude is "somewhat smaller" and the calibration is not deposited. |
| fig2-modulated-locks-to-beats | partially_reproduced | (i) At most 10 APs per session. (ii) 85–100% of APs fall in the middle half of the beat (cell 33), and the histogram peaks at 20–35 ms (cell 34). (iii) The claims' block test was never computed for modulated sessions; the notebook's O4(a) test flags one session. |
| fig2c-pure-more-aps | reproduced | ROI c: pure sine has more APs in 47 pairs, modulated in 0, paired p ≈ 3e-10, under both AP readings (cell 36). Pure exceeds modulated under every reading; only the eroded-ROI + 5 SD readings miss p < 0.05. |
| fig3b-low-conductivity-halves-threshold | blocked (data_missing) | Confirmed in the archive: no 250-ms NaGlu sessions. 001031 is in NaGlu but holds 100-kHz bipolar pulses for 2 s, and an archive search for "gluconate" finds nothing. |
| fig3c-sustained-firing-2s | not_reproduced (provisional) | Part (iii) fails in all 4 neurons under every reading: APs are detected after 275 ms at the top voltage, e.g. c7 at 2.3 V has 11 APs on a 6.7% mean dF (cell 39). The detector counts plateau oscillations as APs (problem 3), so this could flip. |
| figs1-di8-anepps-control | blocked (methods_underspecified) | The readings disagree: ROI c latency falls with field in 1/3 neurons (O3 a) vs 3/3 (O3 b) (cell 41). Only 3 of the 8 neurons are deposited, and the claims' block test was not computed. |
| figs2-ttx-blocks-depolarization | partially_reproduced | APs are abolished in 6/6 TTX neurons (ROI c, cell 44). The depolarization half is untested: a sustained depolarization before TTX is found at the common voltages in only 1 of 6 neurons. 11 of 13 "vehicle" neurons keep their response. |
| fig4-orientation-time-constants | blocked (metadata_insufficient) | No ROIs (O1) and no shape or orientation labels; confirmed by scanning all 001273 session descriptions. There are 22 replicate groups against the paper's 19 experiments. |
| fig4-no-pole-difference | blocked (metadata_insufficient) | No ROIs (O1). The variant run over 22 groups gives paired p = 0.053, 0.105 and 0.917 (cell 54). |
| fig4-discharging-slower | blocked (metadata_insufficient) | No ROIs (O1). The variant gives per-pole p = 0.12 and 0.37 (cell 54), so it would fail anyway. |
| fig4-pooled-time-constants | blocked (metadata_insufficient) | No ROIs (O1), and which 19 experiments are the paper's is unknown. The variant has 0 of 4 values within the SEM in all 8 runs, and 16 of 176 fits sit at the 20-µs bound (cells 53–54). |
| fig5-carrier-antiphasic | blocked (metadata_insufficient) | C7 cannot be matched (O4): no cell has 12 sine sessions at both rates, and the descriptions carry no cell labels (checked via the API). There are also no ROIs. |
| fig5-whole-cell-depolarization | blocked (metadata_insufficient) | Same reason as fig5-carrier-antiphasic. |
| fig5-sine-asymmetry-c7 | blocked (metadata_insufficient) | Same reason. |
| figs3-sine-asymmetry-c8 | blocked (metadata_insufficient) | C8 cannot be identified, and there are no ROIs. |
| fig5fg-no-migration | blocked (metadata_insufficient) | The dataset holds none of the 16 ROIs or their 5F/5G split. |
| fig6b-pulse-sensitivity | blocked (metadata_insufficient) | The dataset has no ROIs, and O1 says to block in that case. The rebuilt-ROI variant gives a mean of 17.4 against 28±2.5, with a minimum of 3.1 (cell 57). |
| fig6c-sine-sensitivity | blocked (metadata_insufficient) | O1. In the variant, 4 cells (or 0) have p < 1e-4 in both ROIs, against 8 in the paper. |
| fig6d-sine-less-than-pulse | blocked (metadata_insufficient) | O1. The variant gives a sine mean of 5.6–8.3 and a sine/pulse ratio of 32–47%. |
| threshold-depolarization-estimate | blocked (metadata_insufficient) | It depends on fig6d and threshold-2khz-unmodulated, both blocked. |

### B. Problems

1. **[affects a conclusion]** The whole notebook follows another claims file (claim ids, readings O1–O6). These claims of this file are only covered by side outputs under other names, not tested under their own ids: fig1-onset-delay, fig1-max-rate-ceiling, threshold-2khz-unmodulated, fig4-no-pole-difference, fig4-discharging-slower, fig4-orientation-time-constants, fig5-carrier-antiphasic, figs3-sine-asymmetry-c8, fig5fg-no-migration.
2. **[affects a conclusion]** `detect_aps`: the AP readings are not the claims file's. Claims reading (a) has no width limits; the helper adds a 2–20 ms half-width, a 5-ms separation and a 5 SD alternative. Claims reading (b), a rise of ≥5% within 5 ms, is never run. This touches every time-lapse claim.
3. **[affects a conclusion]** `detect_aps` uses an absolute height of 5% with no prominence requirement. In a synthetic test, a 7% plateau carrying 1% oscillations gave 11 false "APs". This defeats the block tests in cells 20, 33, 38 and 44, which require "no AP".
4. **[affects a conclusion]** Cell 11 markdown: where readings disagree, ROI reading (c) decides. The claims say to block as methods_underspecified in that case.
5. **[affects a conclusion]** Cell 20 (`block`) is not the claims' fig1-excitation-block criterion. The notebook uses its O4 test, only neurons tested above their best-rate voltage, and an added post-stimulus condition. The outcome is the same (not reproduced) when judged from cell 21.
6. **[affects a conclusion]** There is no bleaching correction for the 250-ms traces. `mean_post50` is mostly −0.5% to −4%, so late-window dF is biased downward. This affects fig1-excitation-block, figs2 and fig2 part (iii).
7. **[affects a conclusion]** First-AP latencies go down to 1 ms (cell 18), and the 0–10 ms bin of 001033 holds 45 APs (cell 9). These may be stimulus-onset artefacts; they were never inspected, and they pull down the median latency for fig1-onset-delay.
8. **[affects a conclusion]** Cell 44 (`ttx`): `ok` checks only for any response before and none after. It never tests the claims' condition (last-100-ms dF >5% before, <5% after). The vehicle split at the longest pause uses gaps of 35–167 s for some neurons (17_20240801, 13_20240731, 4_20240730), not "about 5 min".
9. **[affects a conclusion]** fig2d tests (cells 25, 30): thresholds in nominal volts are compared across frequencies even though the files state the calibration is frequency dependent. The 20-kHz modulated groups have n = 3 (1 AP) and n = 2 (5 AP).
10. **[affects a conclusion]** Strobe sections (cells 52, 56): rebuilt 12×12 box ROIs and whole-image-median scaling are used as tests, where the claims' O1 rule says to block. Within those variants:
    - LOESS is statsmodels `lowess` (locally linear, 3 robustness iterations) with frac 0.2 and 0.4, not O2's R loess with degree 2 and spans 0.75/0.5/0.25.
    - O3(b) without an intercept is not run.
    - The field's carrier phase is assumed to be 0 at frame 0 and never checked. The ROI 1–ROI 2 oscillations are positively correlated in 6 of 9 cells (cell 61), which suggests a common-mode signal or a phase mismatch.
11. **[affects a conclusion, variants only]** The field per cell is scaled linearly with voltage (0.136·V/7 and 0.257·V/10; one cell's pulse was at 15 V). For 001273, the descriptions give measured amplitudes (40 V→25 V, 80→62, 100→79, 130→102), which the notebook ignores when pooling groups at different voltages.
12. **[does not affect a conclusion]** Cell 59 uses a ±1.1 mV tolerance and a 4.5–16.5 mV range; the claims file gives ±0.68 mV.
13. **[does not affect a conclusion]** Cell 33: beat-phase reading (b) and the "near > 0.5" threshold are not the claims' (which use 80%). The pass on (ii) holds at 80% anyway.
14. **[does not affect a conclusion]** Cell 41: the "sustained" test accepts sustained firing *or* depolarization, not the claims' block test. Cell 53: fig4-pooled reading (b) is not run. Both claims are blocked regardless.

### C. What I could not check, and the output that would have let me

- **fig1-pure-sine-excites-all:** per-neuron excitation under the claims' two AP readings, i.e. the 20-kHz count under a plain 5% peak with no width limit, and under a ≥5% rise within 5 ms.
- **fig2 part (iii):** the number of modulated sessions with last-100-ms mean dF above 5% (and above the near-threshold value).
- **figs2:** per TTX neuron, the last-100-ms mean dF before and after TTX at the matched field.
- **fig1-onset-delay:** the traces or AP prominences of sessions with first-AP latency under 5 ms.
- **fig3c:** prominence of the post-275-ms "APs" for c7 at 2.3 V and c8 at 2.0 V, and the result under the rise-within-5-ms reading.
- **Strobe variants:** the pulse-onset frame of the 140-frame 001274 pulse files (their file-level description was not printed), and a carrier-phase check such as a cross-correlation of the subtracted trace with the assumed field.
- **Figures:** I could not view the notebook's plots (cells 18, 39, 42).
