I've addressed all of the round-1 report. One outcome changed (ed9c), outputs were added for every request I could fit in the time limit, and the entry re-runs clean: `entry.py all` passes in 23.6 minutes. Two consecutive runs gave identical numbers. Nothing is committed.

**Outcome changed**
- **ed9c-local-decoding-map: not_reproduced → reproduced.** The verifier suspected the SGD solver (problem 2), and it was the cause. On the 32-footprint decoders, 10 passes of SGD stop at objectives of 19.8 to 68.9, while the optimum is 1.976 to 2.000.
  - The paper's code leaves the solver at MATLAB's default. For 100 or fewer predictors that is BFGS run to convergence, so the local decoders now use an exact solver (liblinear) with the same objective.
  - With it, 18 of 150 points are significant, and their scores range over 0.075, so the criterion is met.
  - The old SGD solver, on the same points and seeds, gives 1 point and fails. The notes call the result fragile: the optimum is close to the objective of predicting every class absent (2.0), and liblinear hit its 10,000-iteration limit in 2268 of 3000 fits.
  - Round 2 reviews this change.

All other outcomes are unchanged: 6 reproduced, 2 partially reproduced, 7 blocked.

**Added or corrected**
- **Tracking:**
  - Jumps: 2 steps above 40 px between video frames, both from one glitch at 1064.8 s.
  - Small blobs: 55 frames have a blob under 50 px. Dropping them changes the arm label of 0.05% of imaging frames.
  - Sample frames: eight frames with the tracked centroid on the mouse. The one at 102 s, in the excluded opening part, shows a gloved hand. The text about the experimenter now says only what these frames show.
- **fig2 solver check:** six splits fit by both SGD and the exact solver. The exact solver gives lower accuracies (0.262 to 0.318 for real decoders, 0.131 to 0.164 for shifted ones), still above chance and above every shifted decoder checked. SGD stays for the full-population decoders because MATLAB's default above 100 predictors is also 10 passes of a stochastic solver.
- **ed9c:**
  - Radius set to 45 px, as the criterion says.
  - Null standard deviation per point is shown. A point alone needs z above 3.40; the smallest z among significant points is 2.53.
  - The code's 64-footprint variant now uses the exact solver: 22 of 34 points are significant.
- **ed8:**
  - Random-window baseline: the event's active fraction is above the random 95th percentile for only 6 of 8 components.
  - Random-set spread ratios are 0.951 to 1.042, so any set this large passes. The conclusion now says the test is weak.
  - Event times restricted to after 153 s still pass 8 of 8.
- **ed10:** empirical false-positive count, treating each shifted copy as the data: median 28, maximum 62. None of the 100 copies reaches the observed 100.
- **ed2b/ed2c:** minima at the radius ±5% and about five other centres. For the Kiloscope the minimum runs from 0.695 to 0.831, crossing 0.8 for one of the four moved centres. Outcomes stay as the criterion's centre and radius give them.
- **Determinism:** I seeded liblinear's coordinate order. Unseeded, the exact map's count of significant points changed between runs.
- **Other files:** the helper module docstring, the README row and runtime (24 minutes), the summary and the conclusions are updated. `joblib` is added to the requirements and the lock is redone; no other version changed. The round is recorded under `verifications` for all 15 claims.

**Not done**
- The ed9c map was not rerun with more decoders per point. With 10 per point it already takes 634 s on four cores.
- No paper values for Fig. 2 or ED9b are compared, because the main text is paywalled.
- The Kiloscope pixel size was not varied.
- ed10's slow non-stationarity (problem 5) is not addressed.
- Problems 8 (pixel-size consistency) and 9 (metadata errors) needed no change; I said why in the record.
