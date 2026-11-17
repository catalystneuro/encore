I checked the claims file against the paper and both linked gists, made five corrections, and recorded them under `checks`. The file is ready for an attempt.

**Checker:** `claims/burman-2023.yaml: 35 claims, 34 quotes, 27 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim**
- **The four model claims** (`fig4f-model-hyperpolarizing-less-activity`, `fig4h-model-synchrony`, `fig4h-model-entropy`, `figs7-model-decoding`) **and the opening comment:** the simulation gist ID was wrong. `2ce61e4e790e…` does not exist; the author's gist holding that file at revision f6a05661 is `2ce61e4e57c7659b727d30e3e1e0128f`. I fixed it everywhere it appears.
- **The five dandiset claims** (`fig4c-sample`, `fig4d-synchrony-lower-awake`, `fig4d-entropy-higher-awake`, `fig4-rate-higher-awake`, `figs6-rate-regressed`) **and note N7:** these counted a claim as reproduced if any of the four area and firing-rate readings matched. The Methods and the gist disagree on area selection, the firing-rate formula and the waveform cut. Protocol step 2 says the Methods give the main result in that case and the code's choice is a variant. So each claim is now judged under the Methods reading (A1F1), with the gist's readings run and shown as variants.
- **Note N6:** which neurons form the population for synchrony was left open. The Methods say "all recorded neurons", and the Figure 4C legend uses "recorded neurons" for the 662 kept units. The gist settles it: the population is the selected units before the firing-rate exclusion. The file now says so, with kept units only as a variant.
- **`figs6-rate-regressed`:** if the three regression readings disagreed, the criterion called the claim partially reproduced. I replaced that with the protocol's rule: the author adopts the reading the paper best supports and marks the outcome as resting on it.
- **`fig4f-model-hyperpolarizing-less-activity`:** the "lower in at least 18 of 20 runs" rule is not in the paper. The activity comparison now uses the paired t test over pooled neurons, which the paper applies to the model's other per-neuron measures in Figure 4H. The per-run count is still reported.

The rest checked out:
- **Statements and statistics:** the statements, quotes, statistics, n's, expected values and tolerances of the patch-clamp claims (Figures 1 to 3) match the legends and Results.
- **Gists:** the analysis gist matches notes N1 to N7 as written, including the bug where `get_firing_rate` sums spike times where it should count spikes. The simulation gist matches the model criteria.
- **Coverage:** every main finding has a claim, and none comes from outside the paper.

**Still open**
- **Supplement missing:** Figures S1 to S7 and their legends are not in the text, so the tests and methods behind the six supplement-figure claims (S2 to S7), and any reported value for the evoked firing rate, are unread. The readings named for S6 and S7 stand in for them.
- **Paragraph numbers:** I couldn't check the paragraph numbers in the Results sources against the flattened text. The figure panels cited alongside them are correct.
- **Gist hazard for the author:** the analysis gist keys units by the table's row index when collecting spikes, then looks them up by the `id` column. The two agree only if unit IDs equal row numbers.

Nothing was committed or pushed.
