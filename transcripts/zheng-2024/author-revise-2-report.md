I've addressed every point in the round-2 report and re-run the entry: the final `python tools/entry.py all entries/zheng-2024` passed (0 errors) and took 49 minutes. It is still under the 60-minute limit but up from 33, because of the extra electrode-drift sessions. Every conclusion matches the new numbers. Nothing is committed.

**Outcomes:** none changed and none proposed. Three outcomes are now marked as resting on an assumption:
- **fig4-glm-deviance:** its outcome is a judgment on a gap in the criterion; the verifier suggested flagging it.
- **figs14-preexisting-fields-ephys:** the shuffle threshold is averaged over the field's bins, which the paper does not specify.
- **figs1-not-electrode-drift:** the switch time is now flagged as an assumption alongside the amplitude definition.

**Added or corrected:**
- **figs1 (electrode drift):** I added two sessions, e16_3m1_210203 and e13_26m1_211124, a second animal, so it now runs on three of the 11 sessions with wide-band data (about 15 minutes of streaming).
  - Pooled over the three, with peak-to-trough amplitude, at least one test gives p < 0.05 under every switch time:
    - at the trial's start, switching ON p = 0.012;
    - at the entry into the field, switching OFF p = 0.00081;
    - at the code's switch time, switching ON p = 0.019.
  - So the outcome no longer depends on the switch time. It now depends on the amplitude: with trough depth, only the code's switch time gives a significant change (ON p = 0.029).
  - Because the same neighbouring neurons appear in many pairs, I added tests with one value per switch and one per neighbour.
  - I corrected the size wording: the pooled median change is at most 0.8%, and per session at most 2.7%.
  - The record's question to the paper's authors now also asks which moment of the trial the switch time is.
- **figs8:** fixed the code comment that still called per-trial the main reading. The notes now give the per-trial, all-frames values (−0.082 and −0.261) and say that only the familiar p value supports the per-frame reading.
- **Sentences the verifier flagged:**
  - Cell 42 now says all three polynomial orders fall below the expected range.
  - Cell 21 now says 53 units, 52 with slopes.
  - Bin 50 is now described as the first bin past the 111 cm cut, in the return arm, and the thin margin (9.73 against 10.0) is noted.
  - The summary now lists only what the trial-averaged map variant actually re-ran.
  - The data check now prints the units of x and y for each maze, which backs the claim that the novel figure-8 maze has no scale.
- **Code the verifier couldn't check:** I quoted the paper's code in the notebook: the tie rule for picking the number of change points (relevant to fig2d), and the stored outputs and the line behind the figs12 finding that the legend's two windows are swapped.
- **Record:** round 2 is recorded under `verifications`, with all 32 claims, the verifier's reasons in its own words, and my responses. No finding is rated `critical`, so there were no finding reviews to record.

**Not done:**
- The low upstream counts (2,794–2,825 putative switching fields against 3,184) are still unexplained, and I ran no new variant for them; the record says so. This affects switch-step-size-filter, fig2d and multifield.
- The full electrode-drift test, on all 11 sessions (about 78 GB), still does not fit the time limit.
- There is no `questions/zheng-2024.yaml`: the report found no place where the claims file misreads the paper.
