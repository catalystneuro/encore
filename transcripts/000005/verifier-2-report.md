**Verifier report, round 2: Yu et al. 2016 (doi:10.1038/nn.4412) on DANDI 000005 @ 0.220126.1853**

The claims file has 33 claims. The attempt record gives 5 reproduced, 9 partially reproduced, 6 not reproduced and 13 blocked. Cell numbers are 0-based indices of the re-executed notebook.

### 1. Stated outcomes

I agree with all 33 stated outcomes. Three changed since round 1, and I accept all three:

- **fs-touch-response: blocked (methods_underspecified).** This is what I asked for. The header rule ("the outcome is the one they all give, or the claim is methods_underspecified") applies, because (a)(i) and (b)(i) are partial and (a)(ii) and (b)(ii) are not reproduced (cell 46).
- **auc-weak-strong: not reproduced.** In round 1 I said reproduced (fragile). The criterion needs both readings. Under reading (b) the rising group is lower in only 8 of 20 seeds, and the gap is 0.04 to 0.67 spikes/s (cell 91). So the round-1 pass was decided by the seed. The "most of 20 seeds" rule is the attempt's own, and it is correctly recorded as a deviation.
- **auc-groups: not reproduced.** In round 1 I said blocked. Under (b) the reduced-AUC group's response changes in all 20 seeds (p = 0.015 to 0.045). Under (a) the three tests hold in only 9 of 20 seeds. With the seed rule, neither reading matches.

Caveats on outcomes I agree with:
- **thalamus-drives-fs.** Read literally, the criterion says "not reproduced when a test fails". Blocked (too few cells) is the better reading, since 5 cells cannot reach p < 0.05.
- **behavior-false-alarms.** Reproduced only under the most permissive reading, (b)(i). The other readings give 5, 4 and 5 mice. See the claims-file point below.

### 2. Sentences the printed outputs do not support

- **Cell 73, and the attempt record's exc-thalamus-photoinhibition notes.** "so even past the transient the thalamic latency is not the longer one" / "still not longer for the thalamus". This rests on a diagnostic whose cortical threshold is −0.0557 mV per sample, against −0.0206 for the thalamic average (cell 72). Cell 71's own outputs show the opposite: 5.0 against 3.0 ms in 1 ms bins, and the 0.5 ms grand average falls from about 3 ms (cortical) against about 4.5 to 5 ms (thalamic). The outcome does not change.
- **Attempt record, ion-cut-exc-no-touch.** "only 3 more of those 15 lack a clear touch response". In cell 19, anm281589, anm281592 and anm318531 each have spike_input = 1: a cell whose spikes per touch has a 95% interval above zero.
- **README.** "a variant leaves out four mice flagged as lacking touch input". anm275231 has a spike touch input and was flagged on performance (0.46; cell 19).
- **README.** "auc-weak-strong and auc-groups are not reproduced because their readings do not match under most of 20 random seeds". For auc-weak-strong, reading (a) matches in 19 of 20 seeds; only (b) fails (cell 91).
- **Attempt record, exc-vm-touch-whisking, measured value 0.87 mV.** This is the best of the 16 readings, and one of only 2 within tolerance. The main reading gives 0.83 (cell 37). Also, "-61.61" and the earlier 0.74 / 4.36 mV values in the exc-threshold notes are not in any printed output.
- **Minor:**
  - Cell 99 says 5.53 mV; the output says 5.54.
  - Cell 52 says "the diagnostic below", but the diagnostic is cell 50, above it.

Every other sentence of the Result conclusions, the Summary (cell 100), the README and the record's notes matches the outputs.

**Round-1 reasons in the attempt record.** They are faithful paraphrases of my table, with the relevant B-points folded in. They leave out some places where I applied a point:
- B1 (ION-cut cells in the control groups) for fs-touch-response, exc-mainly-touch, exc-threshold and fs-vm.
- B4 (spike detection) for fs-suppress-movement-spiking and auc-groups.

Nothing in them misstates what I said.

### 3. Status of round-1 points

**Resolved:**
- B2: tag rule. The train rule drives the same 24 cells as the old rule, and the 26 untested cells have fewer than 10 pulses.
- B5: the cause of the 0 ms latencies is now shown (cells 50 and 72).
- B6 and B7: the chance level of the r2 rule and the circular PV count are now stated.
- B9: seed check run.
- B10: cortical performance now uses all cells.
- B11: readings O10 and O11 now run.
- B12: held trials of the PV-ChR2 cell are left out.
- B13 and B14: amplitude bias and the single-mouse FS group are stated.
- B15: resampling now averages sample pairs.
- B16: the O3 difference is printed.
- B17: injected current checked; the block holds.
- From section C: pole times, ION-cut candidates, the −50.00 mV median and AUC stability are all done.

**Still bearing on a conclusion:**
1. **ION-cut cells in every control group (B1).** This cannot be fixed. Without the flagged mice:
   - exc-vm-touch-whisking has all four values within tolerance (−60.53 mV, 4.97 ms, 5.54 mV, 1.24 mV), i.e. reproduced.
   - fs-touch-response (a)(ii) has 3 of 3 values within (8.04, 1.82, 5.17 ms; cells 37 and 46).

   So two outcomes depend on contamination the files cannot remove.
2. **Spike detection (B4).** Partly addressed. In the median cell-attached E cell, 5.2% of interspike intervals are under 1.5 ms, and 40 of 50 such cells exceed 1%. A 2 ms dead time removes only 8%, which points to a second unit being picked up rather than double detection. E rates stay 2 to 6 times the paper's; whole-cell E cells also fire 0.70 spikes/s without whisking, against 0.4. This drives the rate failures of exc-mainly-touch, fs-suppress-movement-spiking and auc-groups.
3. **Waveform boundary (B3).** Four driven cells have ratios of 12 to 19, beyond the axis of Supplementary Fig. 6. This split is what makes fs-touch-response blocked.
4. **Untested VGAT-ChR2 cells.** The 26 untested cells count as E. They include a whole-cell cell with 11,087 spikes and 0.37 ms spikes, and a cell-attached one with 16,350 spikes. Both are likely FS, so the E groups probably contain FS cells (exc-mainly-touch, exc-vm-touch-whisking).

**Claims-file issues to report, not correct:**
- **Latency rule (O8).** A 3 s.d. threshold on an unsmoothed dVm/dt at 10 to 20 kHz is crossed by noise: 1 and 3 of the 250 baseline samples already cross it (cell 72). So the latency failures of fs-vm-touch-whisking and exc-thalamus-photoinhibition come from the rule, not from the data.
- **behavior-false-alarms criterion.** "Reproduced … under a reading" contradicts the header rule that readings must agree. Reading (b) also counts anm266945 on one of its 11 sessions (p = 0.003), although its pooled test gives p = 0.305 (cell 95).
- **r2 > 0.25 rule.** As in round 1, the "more than half above r2 > 0.25" rule is close to chance: spikes shifted to the next trial still pass for 16 of 29 VPM units and 9 of 17 FS cells.
