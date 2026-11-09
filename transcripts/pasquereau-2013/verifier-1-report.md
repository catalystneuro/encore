**A. Outcomes** (the claims file holds 28 claims)

| Claim | Outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 24: 115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual, all within tolerance. Counting each merged unit from its first file only gives 112, 49 and 31 before MPTP. |
| monkey-l-perturbations | blocked (data_missing) | Every Leu trial is labelled `not_available` (cell 3). One hold-window command excursion appears in 2048 Leu trials (cell 9). The archive's draft description says "The Leu files contain no perturbation times". Only Leu unit counts could be tested (138/72 against 115/73), and they are not the claim. |
| baseline-rate | reproduced | Cell 27: all six means within tolerance. PTN Mann-Whitney p = 0.020 (< 0.05); CSN p = 0.65. The M1 test is reported (p = 0.0022). |
| ptn-faster-than-csn | reproduced | Cell 29: 18.5 against 3.5 spikes/s, p = 6e-12. |
| antidromic-latency | partially_reproduced | Cell 31: all four means are within tolerance and the PTN p is 0.68. The CSN p is 0.0190, above the criterion's 0.05/3 = 0.0167, so the CSN test fails. |
| false-positive-rate | not_reproduced | Cell 33: 0.228 of cell-directions cross the threshold at the pseudo onset (t-test variant 0.463). The criterion range is 0.0033 to 0.03. Unperturbed trials (0.19, cell 34) and Poisson simulations (0.17–0.21, cell 35; 0.15–0.22 in my own test) agree, so the procedure itself is at fault. |
| torque-related-fractions | blocked (methods_underspecified) | The claims file says these claims are blocked when the false-positive rate is above 0.03. For reference: 1 of 6 percentages within tolerance (cell 38). |
| prevalence-unchanged | blocked (methods_underspecified) | Same rule. For reference: none of the three p values is below 0.0167 (cell 40). |
| ptn-more-responsive | blocked (methods_underspecified) | Same rule. For reference: 70.5% against 16.2%, p = 7e-13; the CSN fraction is out of tolerance (cell 42). |
| one-direction-half | blocked (methods_underspecified) | Same rule. For reference: 52.2% against 44 ± 4.4 (cell 44). |
| excitatory-majority | blocked (methods_underspecified) | Same rule. For reference: 2 of 4 percentages within tolerance; PTN p = 0.34 (cell 46). |
| magnitude-unchanged | blocked (methods_underspecified) | Same rule. For reference: 12 of 12 tests have p < 0.05, with magnitudes smaller after MPTP (cell 48). |
| venus-response-magnitudes | blocked (methods_underspecified) | Same rule. For reference: at most 4 of 8 values within tolerance under any reading (cell 49). |
| latency-shorter | blocked (methods_underspecified) | Same rule. For reference: all 4 KS p < 0.013 and 8 of 8 means within tolerance (cell 51). The t-test variant finds no shortening (KS p 0.17–0.73). |
| latency-not-training | blocked (methods_underspecified) | Same rule. For reference: rho = −0.249, p = 0.0033 (cell 53). |
| fwhm-shorter-ptn | blocked (methods_underspecified) | Same rule. For reference: flexion p = 0.027, extension p = 0.37; 2 of 4 means within tolerance (cell 55). |
| dsi-reduced | blocked (methods_underspecified) | Same rule. For reference: −6.7 points, p = 0.127 (cell 57). |
| venus-dsi | blocked (methods_underspecified) | Same rule. For reference: 3 of 6 within tolerance (cell 58). |
| dsi-not-baseline | blocked (methods_underspecified) | Same rule. For reference: F = 0.40, p = 0.75 (cell 59). |
| kinematics-slower | not_reproduced | Cell 63: peak velocity rises 28% and amplitude 15% after MPTP, under both readings. |
| kinematic-latency-unchanged | not_reproduced | Cell 65: MPTP F = 1037, p ≈ 0 (latencies about 10 ms before MPTP, 3–6 ms after). |
| emg-m2-larger | reproduced | Cell 69: median m2 is higher after MPTP in all three triceps channels, KS p ≤ 5e-15. The torque-size confound in problem 3 still applies. |
| emg-duration-longer | partially_reproduced | Cell 71: 24.6 → 49.4 ms, KS p = 4e-36. Both means are outside 57 ± 6 and 79 ± 3. |
| emg-onset-unchanged | not_reproduced | Cell 71: onset 40.3 → 24.0 ms, KS p = 9e-21. |
| emg-m1-weak | partially_reproduced | Cell 73: after MPTP, m2 > m1 in 96.5% with median m1/m2 0.23. Before MPTP the share is 74.4%, just under the 75% the criterion asks for (median 0.10). |
| velocity-matched-magnitude | blocked (methods_underspecified) | Same rule. It would be untestable anyway: session mean peak velocities top out at 145 deg/s, leaving 0 pre and 1 post responses in 130–200 deg/s (cell 75). |
| session-correlations | blocked (methods_underspecified) | Same rule. For reference: p = 0.19 and 0.023, both above 0.0125 (cell 77). |
| trial-correlations | blocked (methods_underspecified) | The paper gives no single-trial latency; I checked the Methods text. |

Totals: 4 reproduced, 3 partially reproduced, 4 not reproduced, 17 blocked.

**B. Problems**

1. **[affects a conclusion]** Cells 0, 33, 37–59, 75 and 77: the claims file says response-dependent claims are blocked when the pseudo-onset rate is outside 0.0033–0.03. Cell 33 gives 0.228, yet the notebook still treats all 15 dependent claims as tested ("yes" in the cell 0 table). The t-test variant (0.463) does not rescue them.
2. **[affects a conclusion]** Cell 31: the CSN antidromic p (0.0190) is printed with no comparison against 0.05/3. It fails that threshold, which makes the claim partial rather than reproduced.
3. **[affects a conclusion: what the outcomes mean, not the criterion results]** Cell 19 and the kinematics/EMG cells: the torque command differs by state.
   - Before MPTP, 105 of 154 sessions use the smallest pulse (~46 units). After MPTP, 125 of 137 use the largest (~183 units), followed by an opposite swing.
   - This explains faster, larger displacements after MPTP and confounds the m2, EMG duration and EMG onset comparisons.
   - In the middle-size variant (43 pre, 12 post sessions) the m2 rise does not hold (longus 1: 47.6 → 1.3) and duration does not change (p = 0.94). The emg-m2-larger result is therefore not evidence of an MPTP effect.
4. **[affects a conclusion]** `stretch.kinematics`: a 101-tap FIR applied forwards and backwards smears motion about 50 ms backwards in time. In my synthetic test, a ramp starting at 20 ms is detected at 8 ms and flagged as `moving_before`. The data show 241 latencies of 0 ms and 503 trials moving before onset, so latencies are biased early and depend on the pulse shape. The forwards-backwards filter is the claims file's choice; the paper says only "low-pass 25-Hz". The causal variant is also significant (F = 791), so the outcome stands.
5. **[does not affect a conclusion]** Cells 71 and 73: the pre-MPTP "EMG responses" are mostly noise crossings (median duration 9 ms, 63% ≤ 10 ms, median m2 3–5 A/D units). The onset and duration comparisons therefore set noise against real responses. Median m1/m2 also includes channel-sessions with negative m2.
6. **[does not affect a conclusion]** `stretch.dsi` builds P and NP from the largest change over 0–200 ms, whether or not that falls in the response window. The claims file does not set this, so it is the author's choice.
7. **[does not affect a conclusion]** Cell 57: the 2×4 chi-square has a smallest expected count of 1.8. Cell 71's threshold variant drops responses that last to the end of the window.
8. **[does not affect a conclusion; claims-file reading]** The paper's Methods say SDF values were compared "relative to a cell's baseline firing rate (2-tailed t-test)". That reads closer to the t-test variant than to the claims file's main rule (mean ± t·SD, taken from Figure 3). Both give a false-positive rate far above 0.03, so the block holds either way.
9. **[does not affect a conclusion]** Cells 3 and 24: the draft's merged sessions change the counts slightly from the supplementary table (115 against 112 cells, 51 against 49 PTNs, 32 against 31 CSNs). This is explained in cell 6 and stays within tolerance.

**C. What I could not check**

- **Spike window against trial boundaries.** I could not tell whether the −1.8 s spike window, and the −1100 to −600 ms pseudo baseline, fall inside each trial. Spikes exist only inside trials, and trials are separated by gaps, so part of the window could be empty by construction. A printed distribution of (onset − trial start) would settle it. The unperturbed-trial null and the Poisson simulation make this unlikely to change the false-positive conclusion.
- **Per-cell results.** No per-cell table (baseline rate, threshold, latency, sign) is saved, so I could not recompute any group statistic independently.
- **Supplementary table values.** I did not check the claims file's expected values against the supplementary PDF table. Where I checked the main text against the claims file (the 0.002 threshold, the 25 Hz Hamming filter, the |rho| values, the Yates chi-square of 32.3 from 89/131 and 35/114), they match.
- **Command size by state.** Per-trial command step size against kinematics within each state, binned by level, is printed only in aggregate. Pre/post comparisons at matched trial-level step size would show whether any MPTP effect survives the torque confound.
- **Monkey L files.** I checked the archive's description and asset list but did not open any Leu file. Leu blocking rests on the notebook's file scan and the archive's own description.
