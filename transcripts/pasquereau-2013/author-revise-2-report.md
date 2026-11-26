I addressed every point in the round-2 report. The entry re-ran cleanly (`tools/entry.py all` passed in 838 s, check reports 0 errors), and every number in the notes and conclusions matches the new outputs.

**Outcomes**
No outcome changed. The verifier agreed with all 28, and the record keeps them. I did add four proposed changes for a third round to review.

The verifier said the two MPTP states "barely overlap" in torque pulse size. They do share two sizes, though: near 90 units (483 perturbations before MPTP, 227 after) and near 180 units (41 before, 1540 after). Comparing the states at these equal pulses changes four results by the claims' criteria:
- **kinematic-latency-unchanged**: proposed reproduced. With the claims file's onset there is no MPTP effect (p = 0.16 near 90 units, p = 0.98 near 180).
- **emg-onset-unchanged**: proposed reproduced (p = 0.40 and 0.057).
- **emg-duration-longer**: proposed not reproduced. Durations are not longer after MPTP (p = 0.32 and 0.087).
- **emg-m1-weak**: proposed reproduced. The criterion is met in both states at both sizes.

Each proposal states its weakness: few post-MPTP sessions near 90 units (14 EMG channel-sessions) and few pre-MPTP sessions near 180 (5). The causal-filter version of the latency also disagrees near 90 units: it finds post-MPTP latencies about 1 ms longer (p = 0.0027).

I proposed nothing for two claims:
- **kinematics-slower**: at equal pulses the movements are still not slower and smaller after MPTP, so the outcome would not change.
- **emg-m2-larger**: the criterion needs the triceps lateralis, which has only 2 post-MPTP sessions near 90 units and no pre-MPTP session near 180, so it cannot be applied.

**Corrected or added**
- **Notebook text**: I fixed every sentence the verifier said the outputs did not support:
  - The velocity range now holds 2 of 581 session-directions with one response.
  - The 60 to 250 unit range is no longer called matched; the pulses there still differ about twofold.
  - Only the causal filter avoids the onset artifact.
  - The forwards-backwards filter enlarges the latency difference. This corrects my round-1 response, which said it shrank it.
  - The torque pulse ratio is about three times for the means and four times for the medians.
  - The cell counts are within 3 cells of the paper's table, not equal to it.
  - Only one Leu file was timed against task events.
  - The displacements are 2.4 to 3.8 degrees.
- **Exact p**: the latency ANOVA's p is now printed as 1.5e-102, not 0.0000.
- **torque-related-fractions notes**: they no longer name the claim as its own gate.
- **EMG background**: the notes now give the triceps lateralis background and say the pre-MPTP m2 values are close to the noise.
- **Finding 3** (torque pulse sizes): raised from minor to major, as the verifier asked. Its cell now prints the perturbation counts at the two shared pulse sizes.
- **New finding 7** (minor, cell `finding-perturbation-timing`): 88% of Venus perturbations come 1.695 to 1.698 s after the centre target appears, where the paper describes a delay drawn uniformly from 1 to 2 s.
- **README and summary**: rewritten to match the above.
- **Verification record**: round 2 is recorded with the verifier's reasons and my responses, plus its view on finding 3. A note explains that the round-1 cell numbers point to the old notebook.

**Not done**
- No question was added to `questions/pasquereau-2013.yaml`: this round reported no new place where the claims file misreads the paper.
- The round-1 responses that say "matched commands" and "the artifact shrinks the difference" are left as written. The round-2 responses correct them.
- I did not time the other 33 Leu files against task events. The text now says only one file was checked, and the Leu outcome stays blocked either way, because no Leu trial marks a perturbation onset.

Nothing was committed or pushed.
