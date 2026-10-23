I've worked through the verifier's round-2 report. No outcome changed, and for fig4b-speed-correlation-dcp I've proposed a change to not reproduced for a third round. The entry re-ran cleanly twice with identical numbers (2.6 min) and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **fig4b-speed-correlation-dcp:** it stays `partially_reproduced` because round 2 may not change it. Under `proposed` I put `not_reproduced`, because I now agree with the verifier. The criterion needs both groups below p < 0.05. The Anxa1 group is the subject of the claim, and it fails in every reading (p = 0.064 to 0.21). For fig3e the record already treats a failed main part as not reproduced, so fig4b should follow the same rule. The notebook conclusion, summary and README say this change is proposed.
- The other 37 outcomes are unchanged, and the verifier agrees with all of them. It now accepts fig6j-reaching-accuracy as partially reproduced, withdrawing its round-1 objection.

**What I added or corrected**
- **Alignment check for fig4b:** the data check now lists the 19 kinematics files that are off lag 0. Five of them have photometry: two Anxa1, two dLight-dCP and one dLight-cCP; one dLight-dCP file is off by 30 frames.
  - I re-ran fig4b with those five recordings' speed shifted by their lag. Anxa1 p is 0.082 and 0.073, and dLight-dCP p is 0.028 and 0.023, so the result doesn't change.
  - The notebook now prints where each Anxa1 recording's speed-signal correlation peaks. It is within 0.5 s of zero lag in 5 of 10; the others peak between -2.3 and 2.1 s, on both sides of zero.
  - I removed the sentence saying speed and signal are "aligned as run". The text now says they are consistent with one clock where the files allow a check, not shown in every recording.
- **fig4b numbers:** the "without the short recordings" sentence now gives both tests: dLight-dCP p = 0.059 and 0.0499, Anxa1 p = 0.097 and 0.089.
- **fig6c:** the six-point to tail-base speed ratio per group and day is now printed. The text says 1.5 to 5.9 times, correcting "2 to 6".
- **Run time:** the notebook now prints its run time at the end. The README says about 2.5 minutes, and `runtime_minutes` in `entry.yaml` went from 5 to 3.
- **Attempt record:** round 2 is added under `verifications` for all 38 claims, with the verifier's reasons, its outcome and my responses. I also added to the round-1 entry the fig4f value the verifier said had been left out (R = -0.5713 against the -0.572 bound).

**Not done**
- **Event timing for fig3d, fig3e and fig3fg:** I still haven't checked whether a `correct` event's time is the frame where the mouse touches the drop. The videos are external mp4 files, and this environment has no video decoder. That needs a new attempt with one.
- **Mouse 687662:** its genotype conflict between files is still open, because the dandiset gives no way to settle it. fig3d gives the same result without this mouse.
- **Sidak tests:** these still use separate t-tests, not Prism's pooled error term. This is stated in the deviations.
