I've worked through every point in the round-2 report. No outcome changed. I proposed one change for a third round: fig4bc-burst-attenuation from partially_reproduced to not_reproduced. The entry re-ran cleanly (`python tools/entry.py all entries/henze-2000`: 0 errors, notebook passes in 529 s), and every conclusion matches the new numbers.

**Proposed outcome change (fig4bc-burst-attenuation)**
- I kept partially_reproduced and wrote not_reproduced under `proposed`.
- The verifier was right that my selection ignored step length. The median step per cell runs from 0.1 ms (D8131) to 500 ms, against the 350 ms steps of Fig. 4A.
- Cell 58 now also selects on step length (at least 50, 100, 200 or 300 ms), alone and together with the criterion's selection, and runs the criterion's selection without D8131.
- It confirms the verifier's counts: 5 of 10 without D8131, and 3 of 6 for both the full set and the amplitude parts when steps must be 100 ms or more. With steps of 200 or 300 ms it is 2 of 5.
- The selection that uses every feature of Fig. 4A the criterion names is the best supported, and it meets neither the reproduced nor the partial rule. The notes, the conclusion, the README and the question to the authors now say this.

**duration-correlation: dependence on one cell stated, outcome kept**
- Cell 32 now prints each cell's durations for the readings that reproduce, and R with D12821 and D8131 left out.
- Without D12821, no S2 or S3 reading gives a positive R with P < 0.03. The reproducing readings fall to R between -0.197 and 0.545.
- Without both D12821 and D8131, one S3 reading still reproduces (R = 0.654, P = 0.029, n = 11).
- The verifier found the S3 rule reasonable, so I proposed no change. The conclusion, the notes and the question to the authors now state this dependence.

**fig4d-amplitude-correlation: intracellular baseline fixed in `hc1.per_spike_ic`**
- Reading (b) used the mean of -3 to -1.5 ms before the peak. It now uses the mean of the 2 ms before the threshold point, as the claims file defines it.
- The synthetic check in cell 15 gives -60.0 mV against a -60 mV rest.
- D15121 gives R = 0.376 under reading (b) (it was 0.374) and 0.408 under reading (a), both on 958 spikes, so the outcome stands.
- 16 of 64 rows are now positive with P < 0.0001 (R 0.142 to 0.869). The change is recorded as a deviation.

**Text corrections the verifier quoted**
- **Summary:** the spreadsheet covers 18 of the 39 cells and only 2 of the 21 tetrode cells.
- **duration-correlation notes:** the S1 and S4 range is now printed and quoted as R 0.759 to 0.945.
- **First finding:** "six" blocked claims is now "seven".
- **propagation-velocity-range:** the conclusion and notes give both pairings, 0.18 to 0.54 m/s by the fit and 0.18 to 0.60 m/s by the farthest site.
- **Cell 41:** the slope-change description now says first local maximum or minimum, matching the code.

**Record:** the round is in `attempts/henze-2000-01.yaml` under `verifications`. The verifier agreed with all 21 outcomes; each claim has its reason in its own words and my reply under `response`.

**Not done**
- I added nothing to `questions/henze-2000.yaml`, because the report found no place where the claims file misreads the paper.
- Nothing is committed, as instructed.
