I've worked through every point in the round-2 report. No outcome changed, and I proposed one change for round 3, on ed5k. The final `python tools/entry.py all` passed (notebook 48 min, `check` 0 errors), and its outputs are identical to the run before it. Nothing is committed.

**Outcomes**
- **ed5k (generalizes across rank):** still `not_reproduced`, now marked `assumed`. I proposed changing it to `reproduced`.
  - With threshold crossings in either direction, all four train and test combinations give 9 of 9 labels above chance (p = 0.0039).
  - With negative crossings, the main reading, training on subordinates gives only 7 of 9 (p = 0.18).
  - Matched trial by trial, the paper's own input holds 1.06 times the counts of crossings in either direction and 1.47 times those of negative crossings. Methods 17 doesn't say which direction it used.
  - Round 3 will review the proposal, and a new finding asks the paper's authors which direction they used.
- **ed5j (six states):** still `not_reproduced`. On the paper's input at 1 to 10 states, both readings select 6, as the paper reports. On the dandiset input they select 2, or 3 and 4 with crossings in either direction. So the failure comes from the input, not from the ported code.
- **ed5d (latency):** still `not_reproduced` (assumed). The new cut-off sweep (0 to 0.5) shows the outcome depends on how trials are aligned:
  - With each file's best tone shift, p is above 0.05 at every cut-off from 0.2 to 0.5.
  - Without the shift, on the files that line up at the same index, p is below 0.05 at every cut-off except 0.3.
  - The notes, summary and README now say this. A new finding asks the authors how latencies were matched to trials.
- **fig1i:** still `reproduced`.
  - Without the likely misaligned file 20191029-chrimson2-2-2v3, every test still passes (HMM-GLM median 0.693).
  - With z-scored rates at the code's learning rate of 1e-6, AUCs sit near chance and fall either side of 0.5 depending on the seed (median 0.475 with one seed, 0.511 with another). The paper's input z-scored is also at chance (median 0.494). At 1e-4 both decode all 9 labels.
  - That replaces the learning-rate explanation the verifier said was asserted but not shown.

**Corrected**
- fig1i `measured` is now the set actually analysed: 512 trials, 17 files, 10 mice. The notes say this is outside the expected tolerances.
- The Summary now lists which ED Fig. 5k combinations were run on the paper's input; all four are now run.
- Cell 25 now says 67.5% and 75.6%.
- Cell 6 now counts all 53 subject descriptions: 53 mention competition with a cagemate and none mention "alone". The ed8ij, fig2e and ed9b notes cite the count.
- In the round-1 reasons for the fig4a group, I restored the verifier's remark about the API's measured-variable list, which had been left out.
- I recorded round 2 under `verifications` for all 46 claims.
- `hmmglm.py` gained a learning-rate parameter; the default is still the code's value.
- The notebook now takes about 50 minutes, and `entry.yaml` says so.

**Not done**
- The verifier said cell 57 printed -498.757 for one state on the paper's input. Both my full runs print -529.600 with the same seed, so I couldn't reproduce that value. The record gives the current output and the `response` says so.
- I added no reader questions, because the verifier found no place where the claims file misreads the paper.
