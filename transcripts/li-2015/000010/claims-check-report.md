The file is ready for an attempt. The checker passes both before and after my changes: `claims/000010/10.1038-nature14178.yaml: 27 claims, 27 quotes, 13 statistical values, 0 problems`.

**Changes, by claim** (each is also recorded under `checks`):
- **fig2c-selectivity-time-course**: The 200 ms window step decided the claim and 50 ms was only a variant. The paper fixes neither step, so both are now readings, and they must agree.
- **fig2c-population-dynamics**: The statement said the population response "grows more similar to that at the go cue". No sentence in the paper says that, so I cut the statement back to the paper's sentence. Which neurons form the pseudo-population (the 912 selective neurons or all 1,245 putative pyramidal ones) is now named as open. The criterion now says its shape test is a reading made here.
- **fig2e-no-contra-bias-spikes**: Added the spike-count window readings for the t-test. One is the three epochs together; the others are the windows of fig3f-pt-contra-selectivity, where the paper reports the same P = 0.13. Noted that the bootstrap used for the proportions is the Methods' test for Fig. 3f, j, because the paper gives no test for Fig. 2e.
- **antidromic-latencies**: Added the jitters of the activated neurons (2.8 and 2.4 ms). The statement gave them, but the expected values left them out.
- **fig3f-pt-contra-selectivity**: The paper does not say which time a 200 ms window stands for. That can move the onset by up to 200 ms, well beyond the 57 ms tolerance, so the window's start, centre and end are now readings. The 10 ms step is marked as a standard choice.
- **fig4f-spatially-intermingled**: The Methods do not say among which cells the nearest neighbour is searched. Both readings are now named (selective cells, or all cells).
- **fig4h-pt-contra-imaging**: The binomial test was set to two-sided with no source; the sidedness is now named as open. Noted that the text's "approximately a quarter" does not match its own counts (34% and 32%), and that the counts are what is tested.
- **reaction-time**: `expected` was a mapping, unlike every other claim; I made it a list.
- **fig5b-pt-delay-activation-contra-bias** (and the sample-epoch claim that depends on it): Added a third power reading, 0.12 and 0.24 mW, which fits both the legend's range and the text's subthreshold limit. The control-only resampling of Extended Data Fig. 6a is added as a variant that does not decide the claim.

**What remains open:**
- **Figure-only values.** Neither the writer nor I read these from the figures:
  - the significance stars of Figs 1d and 5b
  - the fractions in Fig. 3e, f, i, j
  - the curves of Fig. 2c and Extended Data Figs 3, 6 and 7
- **Decision rules the paper does not give.** Each one is named in its criterion, but they are readings made here:
  - the chance levels in fig2c-selectivity-time-course and ed7-pt-activation-persistent
  - what "spike rate modulation" means
  - the per-mouse rules in ed6d-it-activation-inconsistent
- **No test in ed7-pt-activation-persistent.** The change in population selectivity has no test, so that part can only be described.
- **Coverage.** Every main finding has a claim, and no claim comes from outside this paper. Two minor findings have none: the conduction velocities and the paired-pulse jitter of IT neurons (Extended Data Fig. 5g).

Only the claims file was changed. Nothing is committed or pushed.
