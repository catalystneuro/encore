The verifier agreed with all 34 outcomes, and none changed: 4 reproduced, 1 partially reproduced (tables1-rheobase), 27 blocked for missing data and 2 blocked as too large. The entry was re-run with `python tools/entry.py all` (pass, 13.8 min), the checks pass with 0 errors, and nothing is committed.

**What I added or corrected, by the report's points**
- **Model timing (problem 6 and section C):** the cost estimate for the two model claims no longer rests on a run outside the notebook. A new notebook cell downloads ModelDB 153280 at the pinned commit, compiles it with NEURON 9.0.2, and times a 20 ms run of one network on one core. It took 808 s: 537 s to build the cells, then 12.39 s per simulated millisecond. That makes about 17.4 h per 5 s run and about 677 core-hours for the 39 runs. Because of this cell, `neuron` is now in the requirements, the environment is re-locked, and the notebook's runtime goes from about 1 to about 15 minutes (`entry.yaml` and the README updated).
- **Per-cell rheobase (problem 4):** the notebook now gives each cell's rheobase with spike thresholds of -20, 0 and +10 mV, and the peak of the spike at rheobase. No cell changes. The single spikes of D5_15abf and D6_19abf peak at 46.1 and 42.0 mV, so they are real spikes.
- **SimTracker CellData (section C):** I read its rheobase definition in `tools/CellData.m`: the smallest positive step with any upward crossing of -20 mV anywhere in the sweep. I ran it as a variant and it gives the same per-cell values. The repository is listed under `inputs` with its commit, and the definition is recorded as a deviation.
- **ATF header (section C):** the notebook now prints it. It holds only sweep start times, 5 s apart in every file, and no step onset, amplitude or holding current. So the step onset still has to be found from the voltage.
- **Firing rate reading (b) (problem 2):** the notebook prints that only 2 pyramidal-cell sweeps have a single spike and none has two, and the conclusion says this reading bears little on the firing-curve test.
- **PV34 (problem 5):** the conclusion and notes now say the paper does not name the cell in Figure S3F, so picking the best match of six cells is permissive.
- **Header table (problem 6):** the figs1g-resting-potential row now gives its reason code, data missing.
- **Problems 1 and 3:** no change. The spiking cells, the spike-free variant and the mixed ANOVA were already shown and stated.
- **Attempt record:** round 1 is recorded under `verifications` for all 34 claims, with the verifier's reasons closely paraphrased and my responses. The notes now carry the numbers from the new run.

**Not done**
- No question was added to `questions/crcns-hc-10.yaml`, because the verifier found no misreading of the paper in the claims file.
- Untracked dotfiles and a `scripts` directory sit in the repository root. I did not create them and left them alone.
