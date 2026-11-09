I've worked through every point in the round-2 report. The final run of `python tools/entry.py all entries/001097-liu-2024` passed with 0 errors in 486 s, and the text now matches its numbers. Nothing was committed.

**Outcome changes**
- **fig2e: changed from not reproduced to partially reproduced.** The verifier suspected that choosing the ridge penalty on the last fifth of each training set caused "both" to score below "male", which is what broke the ordering. That turned out to be right. With the penalty chosen by fivefold cross-validation within each training set, the means are −0.041, −0.005 and −0.004 (mouse means −0.026, 0.014 and 0.016). The ordering holds and all three are below 0.25, so the "partially" rule is met, but only just: "both" beats "male" by 0.0003 over cells and 0.0014 over mouse means. The outcome is judged on this penalty choice, which was not set out in advance, and the test is still weak because of drift between folds.
- **fig2f stays reproduced**: 0.477 with the new penalty and 0.450 with the old one, both within tolerance.
- **All other outcomes are unchanged.** The record now has 7 reproduced, 3 partially reproduced, 2 not reproduced and 12 blocked. The claims file has 24 claims; the verifier's count of 25 (13 blocked) is a miscount.

**Added or corrected**
- **m930 duplicate question:**
  - I added two checks covering all seven of m930's oestrogen days: how many male annotation onsets line up with the receptive session, and how well the traces match at the best time shift.
  - Known duplicates match all their onsets (m438 day 1 matches 0.65). Every m930 day matches only 0.13 to 0.21, so none looks like a repeat.
  - The trace match can't tell the m930 days apart (0.62 to 0.81 for all seven), so day 4's 0.73 is not unusual.
  - Leaving out day 3, day 4 or both keeps every Figure 1 value within tolerance; the 1g interval value is 0.217 to 0.219.
  - The previous run had added these checks but left them printing `nan` for every pair whose cell counts differ, which included all the m930 pairs. I fixed that.
- **ed6e:** I corrected 0.62 to 0.61 and now say only the receptive-day value is close to the paper's; the unreceptive values are about twice it. The text now states that on the other factor both mice would meet the criterion, though mouse 543's unreceptive days then ramp too.
- **ed7:** The notebook now prints how much the two factors' weighted cells overlap (23 of 44 shared in m541). The text says m541's other factor shows the same change (30.8 against 17.5 s, p = 7e-6), while 543's other factor does not reach p < 0.05 (p = 0.07).
- **Other text fixes:**
  - Removed the "holds under every design" sentence; the text now says random folds put "both" above 0.25.
  - Corrected fig5c from "5 of the 7" to 4 mice found by the matching rule.
  - Noted in fig3a that the timing and stand-in results can't be checked from the outputs.
  - Replaced the README's unsupported "seven minutes" with the measured run times, and set `runtime_minutes` to 9.
- **Attempt record:** I restored the round-1 evidence that had been dropped (the fig1e counts, the 18 to 75% shuffle pass rate, and the fig2e synthetic null, random-fold null and "both below male"). Round 2 is recorded under `verifications` for all 24 claims.
- **Housekeeping:** I added the missing cell ids to the new notebook cells and restored a lost blank line in `vmhvl.py`.

**Not done**
- The leak of information between neighbouring frames under random folds is not fixed; random folds stay a variant only.
- The fig3a timing and stand-in are not in the notebook, because the `ssm` package does not build in the locked environment.
