I've finished the round-1 revision. Both notebooks re-ran clean with `python tools/entry.py all entries/sennesh-2025` (v1_laminar 18 min, areas 35 min, peak memory 10.7 GB), and `check` reports 0 errors. A development run gave the same numbers, and every conclusion was rewritten to match them. Nothing is committed, and no questions file was needed because the verifier reported no misreading of the claims file.

**Outcome changes**

| Claim | Before | Now |
|---|---|---|
| fig2ab-dd-condition-spectra | not reproduced | partially reproduced (assumption) |
| fig3d-go-gamma-laminar | partially reproduced | reproduced (assumption) |
| fig3h-go-alphabeta-csd-feedback | not reproduced | reproduced (assumption, by a 0.8 ms margin under the Methods' band only) |
| fig4h-ssa-alphabeta-csd | reproduced | not reproduced |

dd-gamma-power-and-peak-only-v1-lm stays reproduced but is now marked sensitive to the seed: the LM power p runs from 0.006 to 0.012 over the five seeds. fig2e, fig3e and fig4def keep their outcome, but the reasons changed.

**What changed in the method.** Three details are now taken from the paper's code (epych at commit cee2e6f) where the claims file left them open:
- **Condition panels (problem 1).** The code draws them as dB of the trial-mean power over the aperiodic fit, the reading the verifier suggested. The old per-trial dB average is still shown as a second reading.
- **Which rows are kept (problem 4).** The code counts every fourth row from the deepest channel and crops off the topmost common row, so a different L1 row is kept. With that row, fig2e shows an L1 alpha/beta increase (0.74 dB with the code's FOOOF range, 1.07 dB with the Methods' range), where the old row showed none. A variant keeping the other L1 row is printed with every claim that rests on L1.
- **FOOOF fitting range for the spectrograms.** The Methods' "2 to 90 Hz with a frequency resolution of 2 Hz" matches the per-mouse spectra, not the 5 Hz spectrogram grid. So the code's 5 to 150 Hz range is now adopted, where round 1 had used 5 to 90 Hz. I made this change myself, not at the verifier's request, and round 2 should look at it.

**Other outputs added for the verifier**
- **Median filter (problem 3).** V1 is re-tested without the filter. The unfiltered V1 values match the areas notebook, and the filtered ones differ by at most 0.09 dB.
- **CSD (problem 2).** The tie-break is now stated in the notebook as an assumption, and the sign of each layer group's mean CSD is printed at every lag.
- **Pupil (problem 8):**
  - The eye clock is checked against the stimulus table.
  - The pupil follows the stimulus sequence more strongly than at random times in all 9 mice with eye tracking.
  - A time-in-session variant reverses the sign of the difference.
- **Smaller points:**
  - Session interval tables: there is no separate habituation table. The first block holds 25 habituation sequences, and `invalid_times` is one empty row per session.
  - The frequency bins' true values are printed (problem 6).
  - Caveats are added for the earliest time bin (problem 5) and for the uncorrected power test (problem 10).

**Record.** The round-1 verification is recorded with the verifier's reason and my response for all 37 claims. Two existing questions for the paper's authors were updated (the fitting range, the CSD bands), and two findings were added: the habituation block holds 25 sequences where the paper describes 50 (minor), and the eye-clock check passed (none).

**Where I kept my outcome against the verifier**
- **fig2g, fig3g, fig3i, fig4g (CSD).** These stay reproduced. When a criterion can't decide because of a tie, the protocol (reader, step 3) says to break the tie as the paper's methods imply, and the paper reads sink onsets by eye.
- **fig2e.** It stays partially reproduced, because with the code's rows the L1 increase is present but below range.

**Not done**
- The kept-row start was shifted by 1 and 3 rows but not by 2, to stay within memory. A shift of 2 keeps no L1 row, so it can't affect the L1 claims.
- I kept suppfig3 as not reproduced. One fitting range gives 4 starred cases, which fits the partial rule literally, but 5 unstarred cases also pass. I read the partial rule as keeping the same limit on unstarred cases, and the notes say so.
