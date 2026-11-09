I've worked through every point in the round-1 report, re-run the notebook, matched the conclusions, notes and summary to the new numbers, and recorded round 1 under `verifications`. `python tools/entry.py all` never got to the run: its check step fails with 25 errors, all in the earlier record `attempts/000005-yu-2016-01.yaml`. That record has no outcomes for the claims added since, and it failed the same way before my changes. No error concerns `-02`, so I ran `python tools/entry.py run`, which passes in 296 s. Nothing is committed.

**Outcome changes (round 1, so allowed):**
- **`fs-touch-response`**: partially reproduced → blocked, methods underspecified. This is what the verifier asked for: with the waveform boundary 2 of 3 values match, without it only 1.
- **`auc-weak-strong`**: reproduced → not reproduced. The verifier had agreed with "reproduced"; round 2 reviews the change. Over 20 further seeds, reading (b) holds in only 8, and the criterion needs both readings.
- **`auc-groups`**: blocked, methods underspecified → not reproduced. The verifier had agreed with "blocked"; round 2 reviews this too. Its three tests hold in 9 of 20 seeds under reading (a) and in none under (b).

For both AUC changes I used a rule of my own: a reading counts as matching only when it matches under most of the 20 seeds. It is recorded as a deviation. Every other outcome stays as it was.

**What I fixed or added:**
- **Tag test:** it now counts every pulse of the 5 and 10 Hz trains. It drives the same 24 cells as before. The 26 cells still untested, including the two with 16,350 and 11,087 spikes, have fewer than 10 short pulses at any cortical site, so no pulse rule can test them. Each VGAT-ChR2 cell is tabulated under three pulse rules.
- **Touch and onset readings (O10, O11):** now run for every claim that uses whisking epochs or onsets, not only `exc-vm-touch-whisking`. No outcome changes.
- **Held trials:** the 13 trials of the PV-ChR2 cell held near 0 mV are left out at rest. Its resting Vm is now -38.8 mV, up from -34.9. The whisking shift toward threshold moves into tolerance, but `exc-threshold-touch-vs-whisking` stays partially reproduced because the touch shift (4.62 mV) is still outside.
- **Spike detection:** whole-cell spikes are clean. In the median cell-attached excitatory cell 5% of interspike intervals are under 1.5 ms, which suggests some double detection. But a 2 ms dead time removes only 8.1% of those spikes, so double detection does not explain the high firing rates.
- **Near-zero Vm latencies:** for touches, the criterion's rule is tripped by single samples of dVm/dt. For both laser latencies (0.10 ms) it is a one-sample drop of about 0.06 mV at light onset, likely an artifact. The first crossing 2 ms or more after onset is 4.9 ms (thalamic) and 5.2 ms (cortical), so the thalamic latency is still not the longer one.
- **Fig. 3 recordings:** I added the injected current per trial for every file. 17 cell-attached files carry a constant stored current of about 1.9, but their traces show no whole-cell slow fluctuations (1 to 100 Hz s.d. at most 0.33 mV, against 1.95 mV for whole-cell files), so the "data missing" block holds. The constant current is added to the existing finding on the current.
- **Other checks:**
  - Pole times are not scaled like `first_touch_time`.
  - The exact -50.00 mV median touch reversal is the mean of the two middle neurons.
  - The two threshold readings (O3) differ by at most 0.009 mV.
  - The 20 kHz averages are now averaged in pairs before decimation.
  - Cortical performance in `behavior-touches` now uses every cortical cell (0.681 and 0.694, within tolerance), with the flagged mice only a variant.
- **ION-cut candidates:** I added the requested cross-tab of VGAT-ChR2 mice by VPM fibre site. It leaves 7 candidates for the paper's 9 ION-cut mice, so the cut mice still cannot be identified.

**What I did not change, and why:**
- **ION-cut cells in every group:** the files do not mark those mice, so this stays a deviation.
- **Waveform measure:** I read Supplementary Fig. 6 and its inset defines peak, trough and duration the way the measure does. Four driven cells have ratios of 12 to 19, beyond the figure's axis; I report this rather than correcting it.
- **Weak chance level of the r2 > 0.25 rule:** that is a property of the claims file, so I report it as a weakness and leave the claim as written.
- **The near-zero latencies** stand as measured, because the criterion fixes the rule. The diagnostics decide nothing.
