I've finished the round-1 revision. The entry ran cleanly from a fresh environment in 46 minutes, `entry.py check` reports no errors, and every conclusion and note matches the final run. Nothing is committed.

**Main change: which units are used.** The report was right that choosing all units went against the claims file's own test (Table I's neuron counts). The paper's 102 sessions can't be found among the dataset's 153, so I compared counts per population and scaled to 102 sessions, for six filters. The filter from the Allen Institute's Visual Behavior Neuropixels tutorial (snr > 1, ISI violations < 1, firing rate > 0.1) matches Table I almost exactly: 0.93 to 1.02 times the paper's neuron counts per area, and neurons per population within 5%. All units come out 1.28 to 1.43 times too high and the claims file's quality filter 0.34 to 0.55 times too low. I adopted the tutorial filter as an assumption, citing the AllenSDK file at a pinned commit. Every claim now also runs under the claims file's two filters. Ten claims would come out differently under one of them, and a table at the end of the notebook shows this.

**Outcomes now:** 12 reproduced, 6 partially reproduced, 20 not reproduced (before: 13, 15, 10).
- **To reproduced:**
  - `fig2a-hippocampus-cv-stable`: under the new filter all seven values are within tolerance.
  - `fig1e-positive-cv-modules` and `fig1e-dg-ca3-anticorrelation-hubs`: these hold when the per-session correlations are averaged. I adopted that combination because joining sessions' series mixes in differences between sessions, as the verifier noted.
- **To partially reproduced:**
  - `fig1c-cv-region-medians`: all medians match and only the spreads (IQRs) miss.
  - `fig2b-visually-driven-js-cv-low`: the verifier's outcome.
- **To not reproduced:**
  - `fig4b-thalamus-lgd-lp-modulated`: LP's spontaneous median of 0.098 sits just below the legend's 0.099. Under the other two filters this claim is reproduced, so it depends on the unit filter.
  - `fig4b-other-thalamus-not-modulated`: I now count a nucleus as modulated if any one condition differs from spontaneous, since "all three" was too lenient for a claim of absence. Both tests then find modulation in three or four nuclei. The verifier gave partially reproduced; I recorded that disagreement.
  - Ten more, because their claims have no partial rule, as the verifier read them: `fig1e-midbrain-weakest-cv-correlations`, `fig2a-midbrain-cv-invariant`, `fig2b-dg-ca3-high-js-cv`, `fig3c-vis-ch-plane`, `fig4a-vis-complexity-by-condition`, `fig4e-js-complexity-natural-images` and the three Fig. 5 coupling claims (visual cortex, thalamus, midbrain).

**Other report points:**
- **Fig. 3a reference systems:** the Ikeda map is now judged at its usual chaotic value shifted into the paper's range. It lands just below the range (C 0.355 against 0.36). "H near 0" for the sine is now read against the lowest value a sine can reach (0.105), at three samplings. The claim stays partially reproduced.
- **Added outputs the verifier asked for:**
  - all six pairwise p-values per thalamic nucleus;
  - a session breakdown (no grouping by genotype, image set, novelty or probe count gives 102);
  - flashes per image and blank-piece durations (median 286 s against the paper's 240 s);
  - JS divergence in natural logs;
  - one-value-per-population tests alongside the window-level ones;
  - C-H spans compared before rounding.
- **No changes needed:** points 5, 7, 8 and 10 didn't affect any outcome. The effect forms and readings are kept and shown.

**Record and questions:**
- Round 1 is recorded under `verifications`, claim by claim, with the verifier's reasons and my responses.
- I updated four findings with the new numbers and added one at the end asking how the paper combines sessions for Fig. 1d and 1e. The others keep their order.
- I created `questions/paula-2026.yaml` with two questions for a reader. One asks about the claims file's presence-ratio cutoff (0.9 against the 0.95 the verifier cites) and whether the tutorial filter should be a reading of its own. The other asks how "H near 0" should be read for the sine.

**Not done:** I didn't read the figures (the PDF still couldn't be rendered) and didn't add a third way of combining sessions for Fig. 1d.
