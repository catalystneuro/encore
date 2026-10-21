I've worked through every point in the round-1 report. No outcome changed, and `python tools/entry.py all entries/001636-pasquereau-2013` passes with 0 check errors and a 175 s run. The re-run printed the same numbers as before, plus one new line, and the conclusions match them.

**Outcomes**
- **`false-positive-rate`:** I kept this as blocked (methods_underspecified) and recorded the disagreement; the verifier would call it not reproduced. Protocol step 5 says that when a computed false-positive rate is far from the paper's, the procedures differ and the outcome is blocked even though the analysis ran. The verifier's own reason, that a single run cannot tell a wrong claim from a different procedure, is the case that rule covers.
- **Everything else:** the verifier agreed with all 27 other outcomes.

**Added to the notebook**
- **Monkey L check (asked for):** a table of torque-command excursions for every file. The 35 post-MPTP monkey L files with a command have 91 to 413 excursions each, starting 0.31 to 0.84 s after the lateral target, during the active movement. Only 1 of their 2048 trials has one in the hold window. In monkey V such excursions start in the hold window in 1811 and 3563 trials, against 1862 and 3649 labelled perturbations.
- **Angle scale check (asked for):** active movements measured with our filter are within 2% of the files' own peak-velocity and amplitude columns (Spearman rho about 0.99) and match the 20 deg targets. So the small torque-evoked movements (3.09 deg against the paper's 10 deg) are in the data, not an artefact of our measure.
- **Detection diagnostics (asked for):**
  - Synthetic Poisson spike trains give the same false-positive rate (0.15 main, 0.49 for the t-test variant).
  - The rate stays at 0.17 to 0.27 across baseline-rate quartiles and 0.21 to 0.24 across trial counts.
  - Example mean SDFs are drawn with their thresholds.
  - 14 cell-directions have no baseline spike and can never respond.
  - A threshold calibrated to a 0.01 false-positive rate finds about 31% of M1 cells torque-related, further from the paper's 75% and 68%.
  - Taking the first crossing anywhere in 0 to 200 ms as the onset removes 6 of 202 responses.
- **Movement latency variants:** a causal velocity measure that cannot shift onsets earlier, and a version without the trials already moving before onset. 219 of 5413 perturbations have a 0 ms latency. Latencies are still shorter after MPTP (F = 743 to 1037); with only the middle torque-command size, the causal measure gives p = 0.25.
- **Smaller additions:**
  - `dsi-reduced`: a variant with categories set from the DSI value (p = 0.42), and the smallest expected count of the main table.
  - `emg-duration-longer`: 63.6% of pre-MPTP EMG durations are 10 ms or less.
  - `emg-m1-weak`: the m1/m2 ratios over sessions with m2 > 0 are now in the conclusion.

**Corrected**
- I deleted a stale duplicate conclusion under `torque-related-fractions` that gave different percentages (47% and 52%).
- The conclusions for `emg-m2-larger`, `kinematics-slower` and `kinematic-latency-unchanged`, and the summary, now say these differences cannot be attributed to MPTP, because the torque command is about four times larger in most post-MPTP sessions.
- The attempt record has updated notes, two new deviations (the DSI category rule and the onset reading), and the round recorded under `verifications` for all 28 claims.

**Not done**
- **Torque actually applied:** this can't be checked. The archive has no torque-sensor channel, only `ElbowTorque`, which is described as the commands sent to the torque controller.
- **`trial-correlations`:** still blocked. A single-trial latency definition chosen here would be a method the paper does not give.
- **Plots:** the verifier asked for none.

The changes are in `stretch.py`, `reproduce_pasquereau_2013.ipynb` and `attempts/001636-pasquereau-2013-01.yaml`, not committed. The paper text is in `paper/`, which git ignores. An empty `scripts/` directory and some dotfiles were already untracked in the checkout; I left them alone.
