No outcome changed in round 2, and I did not propose any change. The verifier agreed with all six outcomes. The entry re-ran cleanly twice with `python tools/entry.py all`, and `check` reports 0 errors. Every result statistic is the same as before.

**Fixes for the five passages the verifier flagged:**
1. **Video streaming time (rats-learn-puff-location):** the record had numbers left over from an earlier run (8.1 s, about 217 hours). The rate changes from run to run: 8.3 s and then 7.2 s in my two runs. The record now gives the final run's 7.2 s and about 190 hours, and says the rate varies. The README used to say "more than 200 hours", which the final run no longer supports, so it now says about 190 hours.
2. **"No puffs in the pre-run and post-run" (cell 52):** cell 51 now prints the puffs by epoch. Of 1197 puffs in 38 files, 1195 fall in the run, 2 in the pre-sleep and none in the pre-run or post-run. Cell 52 cites this.
3. **"927 of 957 puffs" (cell 20 and the aversive-direction deviation):** both now say this count covers only the 31 files in cell 19. Cell 48 now prints the count for the 15 tested sessions: 295 of 304.
4. **What makes the ripple-up units a subgroup (cell 40):** this now rests on the fraction being well below 1. The 104 units that fire less in ripples are given as a separate fact.
5. **README run time:** the notebook now prints its total run time (13.9 min in the final run), and the README says about 14 minutes, six of them streaming.

**Round 2 record:** it is under `verifications` in `attempts/000061-girardeau-2017-01.yaml`, with the verifier's reasons in its own words and my response for each claim.

**Left unchanged:**
- **Points already covered:** the verifier raised two remaining weak points but said neither changes an outcome. The thin margin for Rat10 is already in the notes. So is the fact that the ripple-up-cells result holds only under the pooled per-pattern criterion, since the effect is not significant at session level once firing rate is controlled.
- **Lap assignment in cell 51:** the table still assigns laps to epochs by their midpoint, so for Rat08-20130708 its "run" includes the second run. The table is descriptive only and decides nothing, which the record says.

There are untracked files in the repository root (`.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts`, and others) that I did not create. I left them alone; they should be kept out of the commit. Nothing was committed or pushed.
