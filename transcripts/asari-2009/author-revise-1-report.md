I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all entries/asari-2009`. Both notebooks pass (24.7 and 21.6 min) and `entry.py check` reports 0 errors. All conclusions match the final run's numbers. Round 1 is recorded under `verifications`, nothing is committed, and no outcome is under `proposed` because this is the round-1 revision.

**Outcome changes**
- **fig2-example-long-context**: partially reproduced → reproduced. Probe 4 of 20060105-ha1-001-002 meets the criterion's rule. It was picked from 20 candidates and its late period lasts only 60 ms; the notes say both.
- **fig3b-fractional-power-decay** and **fig4-predictability-upper-bound**: partially reproduced → not reproduced. The time constant is outside tolerance under every reading, and the criteria have no rule for partial.
- **fig8c-relative-effects**: partially reproduced → not reproduced. I ran the natural-sound reference without silence, as the verifier asked, and fixed the partial check, which had left out the requirement that amplitude and frequency reach 1. In every reading the amplitude and frequency ratios are below 1.
- **fig4-strf-performance-low**: blocked → not reproduced, now tested in a new notebook `strf_wehr.ipynb` with helper `wehr_strf.py`. It uses the 16 of Wehr's 25 cells that have repeated sounds; the paper used 20 and doesn't list them.
  - Performance is low: at most 0.21 in the main reading.
  - Lengthening the window from 180 ms to 4 s gives a small but significant gain (STRF p = 0.011, LN p = 0.042).
  - With whole stimuli as folds the gain is not significant, but LN reaches 0.241, above the 0.22 bound.
  - So no reading meets the criterion. The outcome rests on the cell selection and the claims file's test.
- **Kept, with the verifier's disagreement recorded**: fig7 stays blocked as `data_missing`. A fuller search prints every DMR, TORC and SoundTrans stimulus, and no recording has the three single bands. The weaker check is now run: 3 of 10 tests have a significant period ending at or after 3.6 s.

**Corrections**
- **Figure 8 property sets** (the verifier's main point): the AM and FM sets were wrong. Each set is now counted as its own test for AM and FM, AM-mean variants are treated as AM (as the recordings' own notes do), and SoundTrans frequency shifts are now detected. This reproduces all five Table 1 totals exactly (95, 110, 96, 82, 137). The two other readings are shown alongside. Outcomes for fig8a, fig8a-significance-fits, fig8b and the natural-versus-synthetic test are unchanged.
- **Firing rates**: added the baseline and probe-period windows and a second MGB detector threshold, 32 readings in all. None has all four means in tolerance, and the rule for partial now holds in 28 of 32.
- **Smaller points**:
  - The notebook lists the 96 synthetic-sound cells behind 133 versus 123, but that doesn't identify which cells the paper counted.
  - Every significant period is now printed for the fig2 candidates.
  - Fits stuck at the 100 s bound are flagged.
  - The running average now ignores bins where no probe is running.
  - Each property set's trials are cut using only that set's contexts.
  - The 51-point run rule and the 200 shuffles for the without-silence variant are now stated.
- The record's findings, the README and the summary tables are updated.

**Not done**
- The trial-resampling reading of fig8c: the per-file pass doesn't keep single trials.
- No reader questions: the verifier didn't report anywhere the claims file misreads the paper.
