No outcome changed: still 5 reproduced, 3 partially reproduced, 31 not reproduced and 3 blocked. I wrote no `proposed` entries because no outcome needs one. The final `python tools/entry.py all entries/jones-2021` passed (rest 41 min, run 29 min, CSD 6 min), `entry.py check` reports 0 errors, and every number in the conclusions matches that run. Nothing is committed.

**What I found while answering the stability question.** The model fits stop short of the best fit (the likelihood maximum) for the frequency features, which have one value per oscillation peak and up to millions of values per group. Where they stop differs from run to run. That is why the verifier's run printed different values from the one my text was written from. The worst case is fig6g's one-site DG result: p = 2.2e-08 in my runs, 0.33 in theirs. Several of the "wrong number" points (2b, 2c, 2d, 2e, 2g) come from this; in the run now deposited the printed values are the ones the text gives.

**What I added**
- **Optional refit in `jones2021.py`:** a `polish` option on the model fit continues from the best starting point until it reaches the maximum. On the hardest cases it matches a dense grid of starting values, and it gave identical results in all three runs I made.
- **A "Fit check" section in the run notebook:**
  - It refits all 660 run tests. 12 significance decisions change and no outcome does.
  - For fig6g, both frequency readings (pooled over sites and one site per region) now give CA3 and DG but not CA1, so it is partially reproduced either way.
  - It prints the fitted random-slope variances and tests with mice as the unit, as the verifier asked. figs5-theta-coherence-frequency, tables4 and fig6g hold per mouse in direction, but most would not survive multiple-comparison correction (Holm over 36) with mice as the unit. The notes say this.
- **fig5b:** the notebook now prints which mice have shifted spike times. PV-Cre has them only for vehicle sessions and SST-Cre only for CNO, so neither group can be tested.

**What I corrected**
- **fig6g:** now marked `assumed: true`, with a deviation, and the one-site statement is rewritten.
- **figs3-dentate-spikes:** the conclusion, notes and question for the authors now say the 8.58/s rate matches Table S4's 9.18 and 8.45 Hz. The question now asks about the amplitude units.
- **fig4d:** the empty vector rise may come from z-scoring or from session order; the text says no output separates the two.
- **Other text fixes:**
  - fig5f now gives the genotype p-value range with 5 degrees of freedom as well.
  - tables4 now says the one-site variant is untransformed. Logged, the CA3 one-site difference is significant.
  - The rest notebook now says "22 of the 24" rest features.
  - The cohort 3 finding now says 4 rest and 9 run features.
  - The running-speed wording is fixed.
  - The README now covers fig6g's assumptions and the fit check.
- **Record:** I recorded round 2 under `verifications` for all 42 claims. I also corrected round 1's `reviewed` text to note the result cells that were left in.
- **Kept with disagreement recorded:** tables2-rest-sg-pv stays partially reproduced; the verifier's strict reading would make it not reproduced.

**Not done**
- The rest notebook's fits were not refitted. It already runs close to the 60-minute limit, and the README says so.
- The track issues left over from round 1 were not analysed further: 48 sessions with a lag more than 2 s from zero, and position ending −92 to +1229 s away from the LFP end.
- No questions were added to `questions/jones-2021.yaml`, because the verifier found no misreading of the paper.
