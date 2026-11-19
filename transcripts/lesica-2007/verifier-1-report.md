**A. Outcomes** (38 claims in the claims file. The notebook tests 36 and marks 2 as blocked.)

| Claim | Outcome | Reason |
|---|---|---|
| sample-composition | not_reproduced | 111 cells pass under reading (a) and 133 under (b), against 68±6.8. The 90 s set has 58/73 cells against 26±2.6. Only the WN/12 s count matches (31/34 against 31±3.1). ON/OFF split is 55/56 against 44/24 (cell 16). |
| firing-rate-contrast | partially_reproduced | Under both P2 readings all four means are within the SDs. Under (a), NS has p=5e-7 but WN has p=0.0022; under (b), NS has p=0.022. No reading gives both p<0.001 (cell 19). |
| firing-rate-lc-ns-wn-similar | reproduced | Reading (a): p=0.063 (>0.05, not >0.2). Reading (b) gives p=0.0013, so the result depends on the reading (cell 20). |
| ln-prediction-accuracy | not_reproduced | r=0.477/0.532 under (a) and 0.282/0.259 under (b), against 0.70/0.76±0.07. n=58, not 26 (cell 22). |
| fig3b-spatial-width-contrast | reproduced | NS p=0.15 (n=110), WN p=0.46 (cell 24). |
| fig3b-spatial-width-correlations | reproduced | −18.9% (P1a) / −20.5% (P1b), p=4e-7 (cell 24). The width difference may be an estimation artifact (problem 1). |
| fig3c-surround-contrast | not_reproduced | NS −11.6% (a), p=3e-5. WN shows no change: −0.6%, p=0.93 (reading b: p=0.50) (cell 26). |
| fig3c-surround-correlations | reproduced | Peak reading (a) with P1(b) gives −37.2%, inside 34±3.4; p=3e-10. Other combinations give 38.7–44.2%, outside (cell 26). |
| fig3d-temporal-width-contrast | not_reproduced | NS +2.4%, p=0.36 (111 cells). WN +43%, p=0.003 (cell 28). |
| fig3d-temporal-width-correlations | not_reproduced | +17.6/+23.3%, p=0.057 (cell 28). |
| surround-temporal-correlation | not_reproduced | r=−0.09 (p=0.18) and r=−0.145 (p=0.03), against −0.5 at p<0.001 (cell 31). |
| figs1-property-correlations | not_reproduced | 1/18 pairs as the legend states under (a), 5/30 under (b) (cell 40). |
| fig4b-gain-contrast | partially_reproduced | Both tests p<1e-9 with LC higher. WN +153.9% (P1b) is inside 148±14.8. NS +124.7/+144% is outside 89±8.9 (cell 33). |
| fig4b-gain-correlations | partially_reproduced | p=3.5e-6 with WN higher. Size +60.5/+66.4%, or 160.5 under (c), against 296±29.6 (cell 33). |
| fig4c-offset-contrast | reproduced | NS −52.9% (P1a), WN −57.2% (P1b) or −64.4% (P1a), all inside tolerance; p=3e-13 and 7e-10 (cell 35). |
| fig4c-offset-correlations-none | reproduced | Adjusted offset p=0.16. The unadjusted variant gives p=0.012, and the pass depends on how the adjustment is applied (problem 2) (cell 35). |
| fig4d-normalized-offset-contrast | not_reproduced | NS +42% (p=1.4e-5), outside 14±1.4. WN −0.08%, p=0.99 (cell 37). |
| fig4d-normalized-offset-correlations | not_reproduced | +50%/+26%, p=0.020, against +90%±9 at p<0.001 (cell 37). |
| fig5-within-trial-contrast | blocked (other: not run) | The data needed (15 min HC movie, spikes, stimulus library) are in the archive. |
| fig6a-reliability-contrast | partially_reproduced | Both p<1e-4. WN 70–75% is inside 74±7.4. Best NS is 48.46% (P8b, P1a), just below the 48.6 lower bound (cell 42). |
| fig6a-reliability-correlations | reproduced | 62.7% (P8a/P1a) and 67.7% (P8b/P1a) are inside 68±6.8; p≈1e-7 (cell 42). |
| fig6b-sparseness-contrast | partially_reproduced | WN 15.7/15.8% is inside 16±1.6, and WN > NS. NS 2.2/2.1% is outside 4±0.4 (cell 44). |
| fig6b-sparseness-correlations | reproduced | 13.1/13.2%, inside 14±1.4 (cell 44). |
| fig7c-effective-contrast | reproduced | Under all four readings, NS ratios (~250–277) are above WN (~72), and LC NS is closest to HC WN (cell 49). |
| fig7d-reliability-tracks-effective-contrast | reproduced | Under stimulus reading (b) the ranks agree and 4/4 are within 1 SD. Under (a) the ranks disagree. The SDs are large, so this is a weak test (cell 50). |
| fig8a-filtered-kurtosis | reproduced | Stimulus reading (a): NS 4.01/3.79 and WN 2.96/2.98 are inside tolerance; shuffled HC NS gives 3.18 (cell 51). |
| fig8-model-sparseness-shuffle | reproduced | Cells a, stimulus a, offset a: 0.810 and shuffled 0.778, both inside tolerance, shuffled lower (cell 52). |
| fig8b-model-vs-experiment-sparseness | reproduced | Two of eight combinations (stimulus a, offset a) meet every condition. The WN H/L model values differ by 0.001 (cells 52–53). |
| fig8de-noise-reconciles | not_reproduced (as run) | No noise level puts all four stimuli within 1 SD. The scan was run only under stimulus reading (b), where the no-noise HC NS model (0.796) already lies outside the SD (problem 4) (cell 54). |
| disc-lcns-hcwn-reliability-sparseness | reproduced | HC WN is higher on both measures: reliability p=0.006, sparseness p=0.0004 (cell 46). |
| disc-lcns-hcwn-rf-nl-differences | reproduced | 3 of 4 at p<0.05; gain goes the wrong way. Only 2 of 4 at p<0.001. Normalized offset passes only with the asymmetric adjustment (problem 2) (cell 47). |
| methods-latency-biphasic | partially_reproduced | Latency is significant in 2/3 comparisons (NS HC→LC p=0.14); biphasic ratio in 0/3 (cell 56). |
| methods-offset-varies-across-animals | not_reproduced | Spatial width, surround, temporal width and gain also differ across animals at p<0.05. At p<0.001, q differs in no condition (cell 57). |
| celltype-y-wider-than-x | reproduced | 0.646/0.743 and 0.642/0.778 deg, p=0.0009 and 0.0001 (cell 59). |
| celltype-y-stronger-surround | not_reproduced | Means are inside the SDs, but p=0.27/0.37 (cell 60). |
| celltype-off-wider-temporal | not_reproduced | ON 37.0 and OFF 35.9 ms, against 25/29; p=0.84 (cell 61). |
| celltype-prediction-x-y | not_reproduced | No significant difference, but the means (0.47–0.55, 0.23–0.30) are far outside tolerance and Y > X (cell 62). |
| methods-spherical-asymmetry | blocked (other: not run) | Needs only the stimuli, which are in the StimulusLibrary asset. |

**B. Problems**

1. **[affects a conclusion]** The ridge penalty (`RIDGE_REL`, cells 8–9, `estimate_rf`) is not the paper's.
   - The paper gives D=0.001 on a stated stimulus scale: zero mean, values in ±106, which is gray levels about 125. That is a penalty of 1000 in the scale the notebook uses, about 0.4× the HC NS variance.
   - The notebook says that scale "cannot be reconstructed". It then uses 10000× the stimulus variance, about 25,000 times the paper's penalty for HC NS. The selection grid (1000–30000) never includes the paper's value.
   - When the penalty exceeds the mean eigenvalue of X'X, the NS estimate drifts toward the spike-triggered average and is not decorrelated. WN estimates are unaffected.
   - Synthetic check with the helper's own `estimate_rf`, same true DoG RF for both stimuli:
     - NS width is 0.756–0.818° against a true 0.644°, while WN stays at 0.644°.
     - The NS surround ratio rises from 0.119 to 0.166.
     - Peak/noise rises from about 9 to 35.
   - This plausibly explains the inflated inclusion count (111 against 68), the NS-against-WN width and surround "correlation" effects, and HC/LC differences, since equal-spike truncation gives HC fewer frames.
   - Problem 1 affects sample-composition, all fig3/fig4/S1 claims, the disc and celltype claims, and fig7–8.
2. **[affects a conclusion]** The per-animal offset adjustment is applied unevenly (cell 33). LC NS is shifted by −280 (Expt1 mean against the two-animal grand mean), while WN offsets are left unchanged because WN comes from one animal.
   - Within the 31 Expt1 cells, adjusting both conditions (identity) gives p=0.012 for fig4c-offset-correlations-none, so the absence would fail.
   - It also moves fig4d's correlation value (+50% against +28%) and the disc normalized-offset test (p=0.005 against 0.056, which drops that claim to 2 of 4).
3. **[affects a conclusion]** RFs are estimated at frame resolution: 12 lags of 16.7 ms, counts per frame (`NLAGS`). The paper bins at 128 Hz with 24 lags of 8 ms, and the claims file's P6 says the 8 ms grid.
   - Temporal widths of about 27 ms, and changes of about 4 ms, are read on a 16.7 ms grid. Latency can only move in whole frames.
   - This affects fig3d, surround-temporal-correlation, methods-latency-biphasic and celltype-off-wider-temporal. It is stated as an assumption, but it is not the method the paper gives.
4. **[affects a conclusion]** fig8de (cell 54) is run only with cells (a), stimulus (b) and offset (a). Under stimulus (b) the noiseless HC NS model (0.796) is already outside the experimental SD (0.801–0.899), so the claim cannot pass there. Stimulus reading (a), the one under which fig8/fig8b pass (0.810), was not scanned.
5. **[affects a conclusion]** 25 of 143 units have HC and LC RFs of opposite sign at their maximal point (cell 16). Latencies of 8 ms and 192 ms also occur (cell 14). ON/OFF labels come from the HC sign alone, and the included set is not screened for these units. This affects celltype-off-wider-temporal and the generic RFs.
6. **[does not affect a conclusion]** The NS RF/NL claims are tested on 111 cells instead of 68, and the prediction claims on 58 instead of 26, because inclusion is lenient (problem 1). On the 31-cell subset, NS surround (−16.8%) and NS temporal width (+16.6%, p=0.043) come close to the paper.
7. **[does not affect a conclusion]** The `pct_change` docstring says (c) is "ratio minus one", but the code returns 100×ratio. The code is the correct reading of the claims file.
8. **[does not affect a conclusion]** P1(b) values for offset and normalized offset (−97%, −139%, +286%) are dominated by near-zero denominators. They are reported but not used.
9. **[does not affect a conclusion]** The helpers `_xtx`, `_half_width`, `fit_rectifier`, `sparseness`, `reliability` and the ridge solve all pass synthetic checks.

**C. Could not check**

- **Fixing problem 1:** the inclusion count and the NS RF properties under the paper's own penalty (λ≈1000 in gray levels, or about 0.4× variance), alongside the chosen penalty, would show whether problem 1 drives the inclusion count and the correlation effects.
- **Fixing problem 3:** an RF estimate on 128 Hz bins with 24 lags would test the temporal claims as the paper states them.
- **Checking problem 2:** offsets adjusted within the 31-cell WN set would show whether fig4c-offset-correlations-none survives an even adjustment.
- **Fixing problem 4:** the fig8de noise scan under stimulus reading (a).
- **Trial selection:** I could not verify which WN HC trial (100 s or 600 s) `_trial` picked in a11/a13/a14, or why Expt1 a12 and b12 were excluded. A per-file inventory output in cell 3 would have settled both.
- **Blocked claims:** fig5 and methods-spherical-asymmetry need no data beyond the stimulus library and the 15 min movie, both in the archive (33 assets confirmed through the API). Both are testable.
