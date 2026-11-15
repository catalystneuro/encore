No outcome changed and none is proposed. Every point in the round-2 report is now either fixed or answered with a new output. The entry re-ran cleanly with `python tools/entry.py all entries/asari-2009` (38 min, 0 check errors), and the conclusions, notes and summary match the new numbers.

**Text corrected**
- **fig3b:** Q is close to the paper's curve only at 0.5 and 1 s. At onset it is 1.039 against 0.49, and the fit's RMS residual over 0 to 1 s is 0.108.
- **STRF, LN:** the Wilcoxon result for LN reflects the 13 of 16 cells that improve. The fold-averaged mean falls from 0.144 to 0.091 and is erratic across windows.
- **methods-recording-counts:** the higher-order shortfall (131 against 137) comes from the natural row (58 against 63) and the MCN row (73 against 74), not from the missing tone probes.
- **The 124-cell count:** the cell 11 label, the conclusion, the notes and the `selection_undocumented` finding no longer say the two left-out designs have no Table 1 column. Both enter Table 1 columns under this attempt's map.
- **Ridge grid:** 54 folds chose the low end of the grid, not 45. The re-run prints 54.

**Outputs added**
- **fig8c:** the natural-sound area is now computed under all four Figure 3B readings. Without silence counted it is 0.597 s, giving 0.91 (0.79 to 1.11) for amplitude and 0.82 (0.71 to 0.98) for frequency. The frequency interval stays below 1, so no reading meets the full or the partial rule and the outcome stays not reproduced.
- **fig4-strf-performance-low:**
  - Stimulus and response share a clock: the sound level and the response correlate most at 24 to 72 ms after the sound in all 16 cells.
  - No response bin falls after the end of its sound.
  - 0.7% of spectrogram values lie below -100 dB (lowest -201 dB). The authors' `logspectrogram.m` has no floor either.
  - The 180-ms filter peaks at its last lag in 7 of 16 cells, not 8 as the report says.
  - The test is now also run over the 10 repeated-set cells, the 6 two-trial cells and the 9 cells whose filter peaks earlier. Each is run with no floor and with floors at -100 dB and at 80 dB below each stimulus's peak.
  - Over all 16 cells every variant still finds an improvement, so the outcome holds.
  - Over the 10 repeated-set cells, neither model improves significantly with either floor. The notes now say the outcome depends on which cells enter the test, and the paper does not list its 20.
- **a1-mgb-firing-rates:** a per-file table and histogram of MGB event heights against the code's automatic threshold.
  - 36% of the events found at 40 SDs lie below it, and they are the majority in 8 of 21 files.
  - They look like spikes: they cluster after stimulus onsets (1,545 after against 143 before) and have spike-shaped waveforms. This supports the lower thresholds.
  - Some files also have a separate low-amplitude cluster that could be a second unit, so the record says this does not prove which detector is right. The outcome still rests on the stated assumption.

**Record:** round 2 is added under `verifications`, with the verifier's reasons closely paraphrased and my replies under `response`. For fig8c it is recorded as `agrees: false` with no outcome, since the report asked for the missing reading without proposing a different outcome. `runtime_minutes` and the README now give the real run time (about 40 minutes).

**Not done**
- No question added to `questions/asari-2009.yaml`, since the verifier found no misreading of the paper.
- The fig8c reading that resamples trials within each probe is still not run. The report did not ask for it, and the notebook says so.
