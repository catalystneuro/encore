I've revised the attempt for every point in the round-1 report and recorded the round under `verifications`. The entry was re-run with `python tools/entry.py all`: the check passes, the notebook runs in about 5 minutes, and every conclusion matches the new numbers. Five outcomes changed; the totals are 5 reproduced, 5 partially reproduced, 6 not reproduced and 6 blocked.

**What drove the changes**
- **Most light pulses are missing from the files (point 1).** In sess9 the gaps between deposited pulses fall only near 20, 40, 60, 80 and 100 ms. A 60 ms gap is a 20 ms offset, a pulse and another 20 ms offset, so a pulse sits there that is not in the file. The files hold 5.8 and 7.5 pulses per second where the protocol implies about 17 to 25. No pyramidal cell on shank Group3 responds to any deposited uLED.
- **Control time is now limited to windows that are dark under the protocol:** the 20 ms before each deposited pulse and the 20 ms after it, about 20% of lap time. The old control time (88 to 90% of lap time) is kept as a variant.
- **Place-field rule (point 2).** `find_fields` is now a direct port of buzcode's `bz_findPlaceFields1D` at the pinned commit. On the verifier's synthetic map (a 6 Hz bump on a 1.5 Hz floor) it now finds the field where the old rule found none. Combining the two changes moves 11 cells between place and non-place; the control time alone moves 5 and the field rule alone 1.

**Outcome changes**

| Claim | Before | Now | New result |
|---|---|---|---|
| figs11 (place-cell fractions) | not reproduced | partially reproduced | 84.2% and 70.6%, chi-squared p = 0.20 |
| fig3a (place cells more excitable) | reproduced | not reproduced | 1.90 vs 1.03 Hz, p = 0.19 |
| fig3g (spatial information) | partially reproduced | reproduced | both parts of the criterion hold |
| fig4c (ripple cofiring, place pairs) | not reproduced | reproduced | rho = 0.060, p = 0.032 |
| fig4d (cofiring with light maps) | reproduced | not reproduced | rho = 0.075, p = 0.25 |

Some of these rest on weak results, and I say so in their notes:
- **fig3g:** I kept the outcome on the control maps the criterion fixed. I recorded the verifier's view that only the time-matched control should count; under that variant the difference disappears (p = 0.3).
- **fig4c:** the effect is weak and comes from sess9 only. The place/non-place pairs show the same coefficient (0.062), so the "absence" there reflects fewer pairs.

**Outputs added at the verifier's request**
- **Metadata now printed:** device and stimulus descriptions, the units columns of all 56 files, and the deposited pulse rate.
- **Response test:** now uses 500 bootstraps. On fake pulse times (jittered by up to 200 ms, or moved into the stimulation-free baseline) 0 of 364 tests pass. Responses are broken down by shank, with the fraction leaving out Group3.
- **Theta checks:**
  - `read_lfp` now reads and checks the stored LFP rate (1250 Hz from 0 s).
  - The clock check is repeated inside the Maze epoch.
  - Control spikes have a mean theta phase of 128 and 130 degrees, which is the trough half of the cycle.
  - Light artifacts in the theta band are small.
- **Uncertainty:** 95% intervals on the fig1e, figs11 and fig3c fractions.
- **New variants:** figs10 restricted to sessions whose first epoch is labelled; fig3f using laps with stimulation only; a labelled figs9 proxy using units at or above 5 Hz. figs9 stays blocked because that proxy splits cells by firing rate, which figs10 shows already predicts the result.
- **New findings in the record:**
  - The missing pulses.
  - A paper inconsistency: 417 non-place cells out of 822 conflicts with 71 to 73% place cells.
  - Some files lack the shank column.

**Not done**
- I could not re-download the paper. PMC returned 429 and 503 errors and Europe PMC a 500, so the `paper/` folder is empty. The 417/822 inconsistency is taken from the claims file and the verifier's report, not re-checked against the text.
- I did not commit or push, as instructed.
