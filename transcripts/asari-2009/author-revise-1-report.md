I've made round 1's changes and re-run the entry with `python tools/entry.py all entries/asari-2009`. It passed in about 20 minutes, and the checks report 0 errors. A second run gave the same numbers, and the conclusions in the notebook, README and record match them. Nothing is committed.

**What changed in the outcomes.** The verifier's main point was that seven claims I had blocked for lack of time could be tested. I tested six of them, and the seventh is now blocked for a different reason:
- **fig4-strf-performance-low: not reproduced** (rests on the criterion's test). A new helper, `wehr.py`, runs Wehr's recordings through the paper's method. Only 16 of Wehr's 25 cells have natural sounds played on two or more trials, which the performance measure needs, so the test is over 16 cells, not 20. Validation performance stays at most 0.22 (0.167 at 180 ms, 0.207 at 4052 ms). But the criterion's Wilcoxon test finds that the longer window improves the model in every reading (p ≤ 0.0005), which counts against the claim.
- **fig7-example-frequency-context: blocked, data missing.** I listed the frequency bands of every DMR and TORC stimulus. No file has the example's three bands, and the criterion says the claim cannot be tested without a matching cell.
- **fig8a-proportion-by-property: partially reproduced** (rests on an assumption). Each synthetic probe is tested only against variants of one property, read from the stimulus parameters. The amplitude and frequency totals equal the paper's (95 and 110 probes), but the significant counts are all low (57, 63, 18, 10 and 45 against 77, 73, 62, 47 and 59). The proportions keep the paper's order, which is the partial rule.
- **fig8b-decay-by-property: partially reproduced.** Amplitude and frequency decay slowly and AM, FM and higher-order decay fast, but no time constant is within tolerance.
- **fig8a-significance-fits: not reproduced.** 3 of the 10 values are within tolerance, and the sizes are not in the paper's order.
- **fig8c-relative-effects: not reproduced.** Amplitude and frequency give 0.74 and 0.67 of the natural-sound effect, and neither 95% interval includes 1.
- **fig8-natural-synthetic-probes-alike: reproduced** (rests on the criterion's Fisher test). No property differs between natural and synthetic probes.

The other twelve outcomes are unchanged.

**Added or corrected at the verifier's request:**
- **Counts:** Table 1 by row and column next to the paper's numbers, cells per synthetic ensemble, and the `probes_m4_nosil` count that was computed but never printed.
- **Firing rates:**
  - A1 rates are now over all 133 current-clamp cells, not just the 39 natural-sound cells.
  - Each spike detector now has a check: spikes per file, the share of intervals under 1.5 ms, and the mean waveform.
  - The 20-SD MGB threshold splits spikes (a median of 23% of intervals are under 1.5 ms). With a 1.5-ms dead time after each spike, the MGB evoked means are still 9.62 and 8.60 Hz, so the partial outcome stands. With the code's own automatic threshold it is still 4.97 to 4.99 Hz, just under the 5 Hz rule.
- **Figure 3A:** the record now says that the count and the paper's chance level are matched under different readings. I also report how often tied values occur (a median of 31% of a probe's time points).
- **Figure 3B:** the long time constant comes from the tail. Q tracks the paper's curve up to 1 s, then sits at about 0.12 at 3 to 4 s against the curve's 0.01 to 0.03.
- **Figure 4:** I ran the 1 − Q reading (time constant 1.29 to 1.78 s, still outside tolerance), and the notebook now flags the fits that stop at the 100 s bound.
- **Supplemental Figure S1:** shuffling gives 3.2 cells by chance against the 19 observed.
- **Figure 9:** without the two cells that failed the clock check, the result is the same.
- **Record:** new findings (missing harmonic-tone probes, the missing Figure 7 cell, the unlisted 20 STRF cells), a question for the authors about the STRF test, and the round-1 `verifications` block. README, `entry.yaml` and the notebook summary are updated.

**Not done:**
- Two of the criteria's alternative readings were not run: resampling trials within probes for the fig8c intervals, and grouping folds by stimulus for the STRF fits.
- I added no questions to `questions/asari-2009.yaml`, because the verifier reported no misreading of the claims file.
