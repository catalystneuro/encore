No outcome changed and I proposed no changes. The verifier agreed with all seven outcomes, and the new analyses do not move any of them under the claims' criteria. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, 6.6 minutes), and every number that was there before came out the same.

**Outputs the verifier asked for (two new cells under flight-spatial-code)**
- **Test on real spike trains cut off from position.** I reversed each unit's real spike train in time within its epoch, which keeps its bursts and rate changes but breaks its link to position. Only 2 of 122 flight ES units come out significant. I also ran Rat3's ES1 spikes against the ES2 position trace and the reverse: 0 of 16 and 0 of 19. So on real trains the test gives fewer false positives than the 0.05 it assumes.
- **What sets the high threshold.** A unit's shuffle 95th percentile is nearly the same for its reversed train (rho 0.995), and 1.7 to 2.3 times that of a Poisson train with the same spike count. It is driven by how few 10 s periods hold the unit's spikes (rho −0.874) and by how few spikes it has (rho −0.601); together these explain 80% of its variance on a log scale.
- **Rat2's FD9 units** are the most clumped in time and have the highest median threshold (3.572). The test has less power for such units, but I did not measure its power. The conclusion and record notes now say that a low fraction of significant units is weak evidence against a spatial code.
- **Rat3's second ES epoch** is explained the same way: TT4/1 and TT5/1 fire fewer spikes in fewer periods there.
- **Earlier-version figures** are now computed in the notebook instead of quoted from the first attempt. On the earlier version's files Rat1 gets 11 or 12 of 25 and Rat2 2 or 3 of 28 over five seeds, with shuffle drops of 0.074 to 0.075 and 0.306 to 0.307. The record now cites these.

**Text corrections**
- **Summary and README:** the false-positive figures now name their null. Poisson trains moved to position sample times give 0.096 pooled and 0.214 at most in one session; plain Poisson trains give 0.074 and 0.160.
- **si-comparable:** "about a quarter" is now "a drop of up to 29% (40% for Rat1 alone) is not excluded", and the text says the result shows only that no difference was detected.
- **fd4:** the text now says that with Rat3's units added, the shuffle-corrected measure is higher on FD4 than on FD9 (0.232 against 0.211, p = 0.31).
- **fig3:** "units with the most stable fields" is now "units whose fields correlate across the epochs", since TT8/5 has r = 0.436, below the median.
- **Runtime:** `entry.yaml` and the README now say 7 minutes (was 5).
- **Record:** round 2 is added under `verifications`, with the verifier's reasons in its own words and my responses.

**Not done**
- I did not add the verifier's round-1 problem 7 (occupancy at 38 to 57 counts/s) to the record. It belongs to no claim, the verifier marked it as not affecting a conclusion, and the notebook already states it.
- I did not measure the test's power, so the record calls it unmeasured.

Nothing is committed, as instructed.
