I've worked through the round-1 report. No outcome changed: the verifier's 22 outcomes all match the record (5 reproduced, 7 partially reproduced, 4 not reproduced, 6 blocked). `python tools/entry.py all` passes, and the final run took 13 minutes. The notebook's numbers match the run's outputs, as do the conclusions, the record's notes and the new `verifications` round (one entry per claim, with its reason and response).

**Outputs added for the verifier's requests:**
- **Curvature (B6):** I added hand paths coloured by class. The classes match the paths, and in J-array the clockwise-curving reaches whose neural state turns clockwise are loops of 162 to 180°. I added a `contiguous` option to `heading_change` and tried thresholds of 10 and 30°. The J-array clockwise class stays at 0.868 to 0.878 under all of them, so the outcome doesn't depend on how the classes are drawn.
- **Phase from the preparatory state (B4):** I added the per-run R² of shuffles 1 and 3, and `prep_prediction_cv`, which refits the whole jPCA for each left-out condition, so nothing leaks. It also adds a phase score that rewards only rotation.
  - Cross-validated R² is 0.615 (J) and 0.727 (N).
  - On the phase score the data beat shuffle 1 clearly. Shuffle 3 still reaches J's value but not N's, so the result stays partially reproduced.
- **J-array frequency (B9):** I added the plane over time, its angular speed, windows starting at -150 to +50 ms, and a synthetic check. The verifier's suspected bias from a window that starts before the rotation does not explain J's 1.03 Hz: windows starting later give 1.04 to 1.13 Hz. J rotates faster before movement onset, and windows starting at -150 or -100 ms give 1.31 and 1.45 Hz.
- **Kinematic models (B3):** I added a `prep_decay_ms` option to `simulate_population`, with variants where the preparatory component is held on or left out, at leads of 100 and 0 ms, plus four more seeds and the angle histograms.
  - The velocity model's angle peak falls near zero (0.028π) only with no preparatory component and no lead, which matches the paper's description.
  - The complex model gets within π/4 of zero in both datasets under none of the choices tried.
  - I kept "not reproduced", because the criterion fixes the model as specified. The notes now say the angle failure comes from choices made in this attempt.

**Text corrections:**
- **Variance claims (B1):** each variance-fraction conclusion now says it compares per-electrode units with the paper's sorted isolations. I also added that deviation to `pc23-variance` in the record.
- **Same-direction claim (B5):** the conclusion now says the counter-clockwise fraction is high for the controls too, because jPCA orients each plane that way.
- **Shuffle controls (B2):** the conclusion now gives the supplement's own expectation for shuffles 2 and 3.
- **Data check:** I corrected the hand-position range to -220 to +165, with targets up to 145.
- **Runtime:** updated in `entry.py` and the README to 13 minutes.

**What I did not do:**
- **Isolation counts and the N-0910 unit count (C1, C6):** these cannot be checked, because the files hold no sort labels or isolation quality.
- **Shuffle controls and smoothing (B7, B8):** I kept the single go-cue dividing time and the missing PC smoothing. They are stated deviations, and the verifier marked both as not affecting a conclusion.
- **Paper text:** I downloaded none, as the verifier's copies were already under `paper/`.
- **Commit:** nothing is committed, as instructed.
