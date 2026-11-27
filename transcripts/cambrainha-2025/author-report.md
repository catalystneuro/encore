I finished steps 1 to 6 on DANDI:000713, pinned at version 0.240702.1725. Of the 18 claims, 3 are reproduced, 2 partially reproduced, 8 not reproduced and 5 blocked. `entry.py all` passed on the final run (notebook 23.8 min, the check found no errors) and the handover package is in `executed/cambrainha-2025/handover/`.

**1. Outcomes**

| claim | outcome |
|---|---|
| sessions-selected | not reproduced (97 sessions from 68 mice, against 62 from 44) |
| fig3a-kurtosis-broader-than-surrogate | partially reproduced, assumed (lowest surrogate kurtosis is 2.80, not about 6) |
| fig3c-scaling-hit-rate-higher | blocked, methods_underspecified |
| fig3c-hit-rate-rises-with-threshold | blocked, methods_underspecified |
| fig3d-relative-gain-24 | not reproduced (largest gain −1.19%) |
| figs1-other-window-lengths | not reproduced |
| figs2-strict-units | not reproduced, assumed |
| fig4a-active-most-scaling | blocked, methods_underspecified |
| fig4-exponents-active / passive / nni | not reproduced (alpha and beta near the paper's values, mu about twice, z about half) |
| fig4bc-static-exponents-trend | partially reproduced (z order fails) |
| figs3-exponents-stable-with-threshold | blocked, methods_underspecified |
| figs4-initial-kurtosis-poor-predictor | reproduced (Spearman 0.178) |
| figs5a-firing-rate-order | reproduced, assumed |
| figs5c-hit-rate-firing-rate-nonmonotonic | reproduced |
| figs7-fatigue-halves | not reproduced, assumed |
| figs8-halves-and-phase-order | blocked, methods_underspecified |

The five blocked claims judge their result over thresholds that start at the largest surrogate kurtosis. Here that maximum is 34.29, set by a few windows, against about 7 in the paper. That leaves the plotted range (up to 12.5 or 15) empty, so the criterion cannot be applied. I blocked them under the protocol's rule that a reference level far from the paper's means the procedures differ.

The notebook also shows each blocked claim over all thresholds from 3 to 15, outside its criterion:
- The hit rate over high-kurtosis windows is below the low-kurtosis hit rate at every one of 236 thresholds.
- The non-natural image phase has the most high-kurtosis windows, where the paper finds the fewest.

**2. Dataset, assumptions, questions**
- **Dataset:** 153 sessions from 81 mice, no duplicates.
  - **Unit counts:** 97 sessions have more than 128 V1 units; with the `good` label 68 sessions (54 mice); with the default quality filters only 1. No reading gives the paper's 62 sessions or its 43 strict sessions.
  - **Block order:** the gray screen comes between the Gabors and the flashes, not last as the Appendix says. One session (sub-585329) has 80.8 min between the active and passive phases instead of about 26.
  - **Trials:** active windows hold 0 to 4 go trials (median 2), against the paper's "three to five".
  - **Clock:** image onsets evoke a V1 response and omitted flashes do not, in every session, so spikes and stimulus tables share a clock.
  - **Version:** this is the only published version, and the draft has not changed since.
- **Assumption:** I adopted CV reading (a), the CV of the population count. Reading (b) would exclude 9702 of 11639 active windows, which contradicts the paper's description of the exclusion as removing rare artefacts. Four outcomes rest on it (marked "assumed"); under reading (b) several of these come out reproduced, resting on 4 to 7 trials.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How is the kurtosis computed so that surrogates reach 6 or more? Followed as written, surrogates here sit around 3.6.
  - Is the surrogate maximum taken over every surrogate window?
  - Which activity is the CV computed on?
  - Over which cluster sizes and ranks are the real-space exponents fitted?
- **Questions to a reader:** none.

**3. Protocol points**
1. The protocol has two rules for readings: "reproduced under any reading" for which trials or subset a number counts, and "they must agree, else adopt the best-supported reading" for method details. The claims file's criteria say "under one reading" for method-detail readings too (the CV, the surrogate maximum). I applied the protocol's rule for method details and recorded it as a deviation. Taken literally, fig3c would be "reproduced", from the CV (b) reading under the claim seed only.
2. There is no rule for a criterion whose threshold grid is empty. I used the chance-level rule and blocked as methods_underspecified.
3. "A claim that depends on a blocked claim is blocked" would cascade from fig3c and fig4a to claims whose own tests could still be run (fig3d, figs1, figs5a, figs7 and others). I applied the cascade only where the block reason carries over and recorded that choice.
4. Seeds for many parallel sessions: the protocol says nothing on this. I gave each session a child seed spawned from the claim's seed.
5. Rating a mismatch between the paper and correct files "about data" fits awkwardly when the paper's description is simply wrong (the block order). I filed it about data, minor.
6. The bootstrap uses 10^4 Poisson resamples instead of 10^5 of fixed size, so that one draw serves every threshold; this is recorded as a deviation.

**4. Runtime and failures**
The run went from 07:21 to about 09:34 UTC. The first full run failed in the exponent section because a variable was overwritten; I fixed it and re-ran (24 min). The re-runs gave identical numbers. In the notebook's data-check text, one sentence says "sessions printed above" where only one session is printed; I fixed this in the record but did not re-run the notebook for it.

Files are in `entries/cambrainha-2025/`:
- reproduce_cambrainha_2025.ipynb
- criticality.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The record is `attempts/cambrainha-2025-01.yaml`.
