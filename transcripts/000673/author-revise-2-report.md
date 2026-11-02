I've finished the round-2 revision. The entry was re-run in full with `python tools/entry.py all`, and the four notebooks passed in 4.3, 44, 23 and 11.4 minutes. The LFP notebook was then run once more on its own, to add the intercepts to the fig2f table. `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcomes.** None changed (still 12 reproduced, 5 partially reproduced, 8 not reproduced, 32 blocked). The verifier was right about the GLM reference level. I refitted the models with load 3 as the reference, which is how Tables S2 and S3 code load. That supports a change for two claims, so I wrote each one under `proposed` for a third round to review:
- **fig3h-pac-category-firing: proposed reproduced.** The hippocampal spike-count term is now positive with p < 0.05 under all four readings (p = 2.3e-10 to 0.031). The amygdala term has p ≥ 0.33. Under single-trial reading (b), the intercept, load and interaction terms are close to Table S3's. The outcome still rests on artefact reading (a); under reading (b), one of the four readings gives p = 0.056.
- **fig2f-rt-single-trial-pac: proposed blocked (`methods_underspecified`).** The outcome depends on how RT is scaled, which the paper does not give:
  - With RT in seconds, neither single-trial reading meets the criterion, and the intercept (1.70) cannot match the paper's 0.38.
  - With RT z-scored within each session, the fit comes closest to Table S2: intercept 0.28, hippocampal term −49.39 with t = −4.19, against the paper's −49.07 with t = −4.01. On that scale, reading (a) fails only because the amygdala term is also significant (p = 0.015), while reading (b) meets the criterion. The criterion treats such a split as `methods_underspecified`.

**Added or corrected:**
- **SFC claims.** fig3f, fig3g, edf5c, edf5d, edf5fg and edf8fgh are now blocked as `other` (not run) instead of `too_large`. I removed the timings, since no output shows them.
- **fig2f text.** I removed the unsupported sentence that Table S2 gives the estimate in ms. The printed maximum RT now comes from the hippocampal trials: 56.3 s, with 87 trials above 10 s. A run that drops RTs above 10 s is also printed.
- **fig3h text.** I removed the "opposite sign" sentence.
- **fig4c.** The notes now say its fits estimate the load 1 slope. I did not refit it, because it stays blocked on the PAC-neuron selection.
- **Smaller fixes:**
  - The session numbers for sub-4 and sub-11 were removed; they were file indices, not sessions.
  - "But one" was removed from the PAC-neuron counts sentence.
  - −3.26 was corrected to −3.27.
  - The README and `entry.yaml` run times were updated.
  - The helper now prints how many times each unsorted unit's spike times step back. This corrected a finding: sub-13 unit 14 jumps back three times, not once.
- **Questions for a reader** (`questions/000673.yaml`): whether the criteria should state that load 3 is the reference level; and whether to drop single-trial reading (a) for fig3h and fig4c, and whether fig2f's criterion should name the RT scale. The finding that asks the paper's authors about single-trial PAC now also asks how RT was transformed.
- **Round 2 recorded** under `verifications`: 57 results, 8 of them disagreeing, each with the verifier's reason and my response.

**Not done:**
- The spike-field coherence claims were not run, as there was not time.
- The gap in PAC-neuron counts (8 and 5 against the paper's 79 and 163) is still unexplained.
- Artefact reading (a) still rests on the one channel whose rejected trials the paper's code includes. No other channel's rejected trials are public.
- edf3e still rests on aligning the windows on gamma peaks; that question to the authors stands.
- The verifier's robustness note (heavy-tailed percentages of baseline) is recorded in the responses, with no further analysis.
