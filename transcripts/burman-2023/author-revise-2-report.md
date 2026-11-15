I went through every point in the round-2 report. None of the 35 outcomes changed and none is marked `proposed`: 5 reproduced, 5 partially reproduced, 25 blocked. The entry was re-run twice with `python tools/entry.py all entries/burman-2023`; the final run had 0 check errors and both notebooks passed (main 152 s, model 1028 s). Every conclusion matches that run's numbers. Nothing is committed.

**Why the decoding statistic changes between runs (figs7):**
- **Cause:** ties among nearest neighbours. The classifier's inputs are small whole-number spike counts. In 80 to 92% of test trials, the fifth-nearest training trial is exactly as close as the sixth, so which five neighbours count depends on how the tie is broken. That differs between runner machines; the random seeds don't control it.
- **Evidence:** a full run of seed 1 here gave accuracies 0.9840 and 0.9424. The run the verifier read gave 0.9820 and 0.9437, with the same synchrony (0.8909). Executions on different runners have printed t = 16.92 or t = 16.42.
- **New check:** `network.decoding_ties` reports the share of tied trials and redoes the decoding with five other orders of the training trials, which break the ties differently. The paired t ranges from 16.35 to 17.22 (p at most 1.20e-12), and shunting is higher in 20 of 20 runs every time. The conclusion doesn't depend on how ties are broken.
- **Text:** this run printed t = 16.42, p = 1.11e-12. The result cell and notes now give that value and name the other one. The seeding deviation no longer implies the run is deterministic.

**Other corrections:**
- **Start-time variant:** a new section in the main notebook now actually prints the sample count (734 kept, 131 excluded), the rate test (14.9 against 8.14 Hz, p = 9.58e-35) and the three regressions (all p below 1e-11). The five deviations now say what it shows.
- **Main notebook summary:**
  - Clocks: it now says they pass in 33 of 34 pairs, and names sub-569069 awake (1.07 times, p = 0.591).
  - Counts: it now names the excluded count (144 against 203) alongside the means.
- **README:** tolerance misses corrected to 0.0011 and 0.0024. Run times now 2.5 to 3.5 min for the main notebook and 17 to 43 min for the model, depending on the runner; `entry.yaml` now says 17.
- **Question for a reader:** I added the verifier's criterion gap for fig4c-sample to `questions/burman-2023.yaml`. The kept count is within tolerance and the excluded count is not, a case the criterion's partial clause doesn't name. The claim itself is unchanged.
- **Record:** round 2 is recorded under `verifications` with all 35 claims agreed, the verifier's reasons quoted or closely paraphrased, and my responses.

**Not done:**
- The two questions from round 1 (whether to judge the Neuropixels claims under the gist's rate, and whether the model tolerances should allow for differences between seeds) are still waiting for a reader. The outcomes stay as tested until they are answered.
- The legends of Figures S4, S6 and S7 are still unavailable, so figs4 stays blocked.
- The schema only allows per-claim entries, so the README run-time point is recorded under dataset-sessions-link (main notebook) and fig4f-model-hyperpolarizing-less-activity (model notebook).
