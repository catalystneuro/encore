I've worked through every point in the round-2 report and re-run the entry. `python tools/entry.py all` passed: the notebook ran in 2,199 s with no errors, `check` reports 0 errors, and I compared each changed conclusion against the new output. Nothing is committed.

**Outcomes**
- **No outcome changed**, as round 2 requires.
- **ed8cd (gain simulations):** I agree with the verifier that it should be reproduced, but the verified partially reproduced outcome stays. Reproduced is now written under `proposed` for round 3. The reasons are:
  - The criterion asks for titrated noise, so the code's fixed noise (1.8 × 1.8 Hz) is only a variant.
  - The comparison against the recorded control cells fails its own check: even the simulation with no gain already differs from them (p = 0.0026 and 0.039).
  - Against the simulated control cells, all three conditions hold (p = 0.022, 8e-5 and 0.13), in 80% of 50 seeds.

  The conclusion cell, notes and Summary row are rewritten to match. The analysis was already in the notebook.

**Added outputs**
- **GLM lags (fig6c):** the paper's code drops a pair with a fit warning at any of 201 lags; only lag 0 was fitted before. A new cell fits 9 of the 27 sessions at four more lags (−10, −1, 1 and 10 s). They flag 60 more HD-HD pairs out of 10,507 (0.6%) and no FS-FS or HD-FS pairs. The HD-HD correlation in those sessions moves from 0.638 to 0.647. This is recorded in the notes, the deviations and the conclusion.
- **Light-pulse series:** every file with one now prints its length, rate, unit, channels and values. The format finding now names A1813 (933,367,680 samples against 233,341,920; 11,667 s).
- **REM inside exploration epochs:** each piece is now printed with its epoch. This corrected a wrong statement in the finding: A1821 has 16 s of REM in the square epoch and 41 s in the optogenetic epoch, not all 57 s in the optogenetic one. A3701 (0.3 s in the triangle epoch) is also listed now.
- **fig1ac:** every 50 µm bin is printed, along with the computed ranges (0.008 to 0.240 over the top 1.4 mm, 0.777 to 1.192 from 1.8 mm down) and the local maxima. The text uses these numbers.

**Text corrected**
- Cell 7: label agreement is 99.9% for excitatory and FS and 99.7% for HD.
- Cell 54: the cumulative signature is above the others at components 1 to 9.
- README: the GLM row now states the assumption about the glmfit copy.

Round 2 is recorded under `verifications`, with the verifier's reasons quoted and my responses. The runtime is updated to 37 minutes. To support the new outputs, `light_pulses` in `posub.py` also records what it reads about the series.

**Not done**
- **The other 196 GLM lags:** all 201 would take about 35 hours, and four lags in a third of the sessions already add 15 minutes to the run.
- **fig6c assumption:** it still rests on the Python copy of MATLAB's glmfit flagging the same fits, since MATLAB isn't run.
- **ed6:** kept as blocked for "other" rather than "data missing". The verifier called this a labelling question only.
- **fig5e and the power reading:** both are left as they were. The fig5e question is already with a reader, and the power reading is a recorded question for the authors.
