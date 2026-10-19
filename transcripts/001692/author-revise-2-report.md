No outcome changed. The round-2 verifier agreed with all 33 outcomes (21 reproduced, 8 partially reproduced, 3 not reproduced, 1 blocked), and nothing I found calls for a change, so no outcome has a `proposed` entry. I re-ran the entry twice with `python tools/entry.py all`. Both runs passed with 0 errors and printed the same numbers, and `entry.py check` also passes with 0 errors.

**Output added**
- **Post-stimulation samples kept (ed9):** cell 102 now prints the share of samples within 3 s after a stimulation that each exclusion keeps. AND keeps 42% and OR keeps none. The text had said that with AND "most stimulation responses stay in the data", which is wrong, so cells 103 and 106 and the ed9 and fig7f notes now give 42%.

**Text corrected to match the printed numbers**
- **fig2d (cell 45 and notes):** the values are now -0.33 against -0.23, -0.19 against -0.16 with p = 0.11, and same-sign p = 0.11 and 0.22.
- **README run time:** now "eight to nine minutes, two to three of them streaming". The two runs took 7.7 and 8.7 min, with 131 and 190 s of streaming.
- **README first row:** now says 127 of the 132 negative sites have DA leading and 31 of the 42 positive sites have ACh leading.
- **Cell 79:** UG27 has 3.4 to 5.4 times as many initiations as each other mouse (92 to 149), replacing "three to five".
- **Cell 88 and fig6a notes:** 2197 is the number of site-trials with a NaN in the search range, so at most that many troughs were missed. The text no longer reads as 2197 misses.
- **Summary (cell 119):** the excitation source descriptions are now said to differ from the Methods, not to be copied from another setup.
- **ed1:** the conclusion and notes now say the controls are organized in space by the paper's own test, since no shuffle reaches the 551 voxels. They also name the two deviations that could add correlated red-green signal: no artifact removal, and only the 15 reward sessions.
- **fig7f:** the conclusion and notes now say the claim's second part (overlap p = 0.065) is not supported, and that the criterion treats it as a variant.
- **fig4c:** the notes now say the difference from the paper's 65 sites is still unexplained.

**Attempt record**
- **Round 1 fixes:** `reviewed` now says the verifier also read the paper and the Zenodo Figure 8 data and queried the DANDI asset list. The fig6a and fig6c reasons now say it classed B6 as not affecting a conclusion. The fig2d response that wrongly said "the values are as before" is corrected.
- **Round 2:** added to `verifications`, with the verifier's reasons and my response for each of the 33 claims.

**Not done**
- **Paper text:** I saved nothing under `paper/`. I didn't download the paper this round, and the copy the verifier mentions isn't in this checkout.
- **Untracked files:** `git status` shows some (`.bashrc`, `.idea`, `scripts`, and others). They are not part of this work and I left them alone.
- **Commit:** nothing is committed or pushed, as instructed.
