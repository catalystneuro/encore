I've worked through the round-2 report. The entry re-runs cleanly (`tools/entry.py all`: pass, 0 errors) and `check` passes. Nothing is committed.

**Outcomes**
- **fig3c-avalanches-emerge:** I kept the verified outcome, blocked (`metadata_insufficient`), and proposed a change to `not_reproduced` under `proposed`. The verifier's argument holds up in a new notebook cell. Of 112 combinations of reading and shift rule, the shift is reached in 77, and in every one of those the exponent is 1.13 to 2.53, outside 1.5 ± 0.15. The exponent is within tolerance in only 14, and in each of those most dishes never reach the shift. Changing the DIV offset alters neither fact, so the missing DIV isn't what blocks the claim. A third round will review this.
- **Every other outcome is unchanged**, and no other change is proposed. For fig3ef I report the formal pass under S1 F1 A2 but keep it blocked. Its Exponential group is two near-silent recordings, and no other fit or size reading passes, so the readings disagree.

**Corrections and new output**
- **"Every active recording":** cells 0 and 10, the Summary, the README, the `methods_unavailable` finding and the first question now say it properly. Under F1, only two near-silent recordings reach b = 0.1. Under F2, most values sit at the bound 0, and two active recordings reach 0.1 (23280 day 2 at 0.464; 23282 day 7 at 0.318).
- **fig1d-shuffle:** added the missing Result cell. It and the record now say the shuffle raises b significantly under three of the four readings (p ≤ 0.0004), but b stays far below 0.1.
- **fig2d-locality-slope:** the notebook now prints the recordings behind the first value of the moving average. The record adds the caveat that the passing readings rest on two near-silent recordings from before their dish's activity begins (14 and 11 electrodes). The sentence about the L2 readings is rewritten separately for S1 and S2.
- **fig3ef:** the notebook now prints whether each reading holds and which recordings make up the Exponential group. The conclusion and notes report the formal pass and how thin it is.
- **fig1d:** the record now says the rank-of-variance variant reaches a majority (4 of 7 dishes) only under S2 F1 with an offset of 1 day.
- **Minor point 6:** under the per-dish offsets O2 and O3, the Spearman tests in fig1b, fig1f and fig2c now use each dish's DIV instead of the recording day. No outcome changes.
- **Stale text:** fixed the old offset lists in cells 0, 16, 32, 38, 44 and 61, and the false statement in cell 32 that the correlation doesn't depend on the offset.
- **Record YAML:** removed the duplicate `outcomes:` key.
- **Questions:** the verifier's report that the claims file misreads the fit added a second question to `questions/002020.yaml`. It asks whether the error should be on raw values (F2), citing the Methods passage and the 4-of-7 result.
- **Verification log:** recorded round 2 under `verifications` for all 20 claims.

**What I didn't change, and why**
The verifier quoted three numbers my re-run doesn't print, so I kept the record's figures and said so in `response`:
- fig3d: the verifier gives a minimum Spearman of 0.0273; the notebook prints 0.0262, so "0.026 to 0.217" stays.
- fig3ef: the verifier gives a maximum of 0.611; the notebook prints 0.617, so "0.62" stays.
- fig2d: the verifier gives ρ −0.384, p 0.036 for S2 M1 L2; the notebook prints −0.329, p 0.076.

These numbers also agree with the earlier run that the record was written from.
