**fig6c-decay-length: the claims file changed.** I added a third reading of the decay length: the time from the signal's peak after onset to the first sample below 0 after it.

- **Why:** the Results define decay length as "the time for the increased calcium signal to return to baseline", and "decay" names the fall after the peak. The Methods only say "the time the z-scored signal was smaller than 0" and don't say where the time starts, so they don't rule this reading out.
- **What changed:** the criterion now says the claim is reproduced when Vgat is longer at p < 0.05 "under a reading", which follows the protocol's rule for readings. Readings (a) and (b), the statement, source, quote and statistics are unchanged.
- **Question file:** the question has its `answer` and `answered: 2026-11-01`.

I decided this from the paper's wording only. The author also reported that the peak-based values match the deposited per-cell values, which I didn't use, since you asked me not to look at the data.

`python tools/claims_check.py` finds all 27 quotes. It reports five p-values it can't match, including this claim's 0.002659548. That isn't new: all five were already flagged and confirmed by hand, and 0.002659548 is in the Figure 6C legend.

Only `claims/001249/` and `questions/001249.yaml` are modified. Nothing is committed or pushed.
