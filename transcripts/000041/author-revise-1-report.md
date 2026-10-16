The verifier agreed with all 39 outcomes in round 1, and none changed in this revision: 8 reproduced, 9 partially reproduced, 15 not reproduced, 7 blocked. I re-ran the entry with `python tools/entry.py all`. The check reports 0 errors, the notebook passes in 232 s, and a second run gave identical numbers. The round is recorded under `verifications` in `attempts/000041-watson-2016-01.yaml`, with the verifier's reasons in its own words and my replies under `response`.

**Outputs the verifier asked for, now in the notebook:**
- **Microarousals:** short Awake epochs counted by the state on each side, and MA counts under five looser rules. No rule reaches both of the paper's values. The closest are 0.177 per min with 7.63% of SLEEP, or 0.245 per min with 13.66% if every Awake epoch inside SLEEP counts.
- **WAKE triplets:** I tried minimum WAKE durations from 40 to 900 s. None gives a sextile 6 increase. At 900 s, 23 triplets remain (the paper had 24), and the change is −0.185 Hz (p = 0.5).
- **Regression to the mean:** the fig2b slope corrected for measurement noise is 0.788, and the fig3d slope is 0.846 (CI 0.812 to 0.881). Both stay below 1, so noise does not explain the effect. I took out the fig3d conclusion's statement that the slope cannot be told from noise.
- **fig3e post-sleep windows:** cutting the pre-sleep window to the same length as the post-sleep one gives the same result.
- **One value per cycle, triplet or session:** these tests weaken two outcomes that I kept, because the criteria decide them.
  - fig3e: sextiles 4 and 5 no longer decrease (p = 0.87 and 0.12).
  - fig4iv: sextile 6 within packets is no longer significant (p = 0.19).
  - fig3-first-last still holds with one value per cycle (p = 0.015).
- **The three sessions with no wake-sleep cycle:** each sleep segment is listed with why it fails. Either the Awake before it is under 7 min, or the recording ends it.
- **Sessions whose clocks could not be confirmed:** a table recomputes every tested claim's main numbers without the one session whose state labels could not be checked against the spikes, and without the seven whose LFP could not.
  - No judgment of the LFP claims changes, and dropping the label session changes nothing.
  - Dropping the seven LFP sessions does change two spike-only claims, though their LFP clock has nothing to do with them. The fig3-first-last last-packet mean becomes 1.006 Hz, outside tolerance, and the nonREM autocorrelogram peak moves to 6.5 ms, outside 7 to 9 ms. The notes say so.

**Corrections:**
- **Autocorrelogram bug:** float rounding put some lags in the wrong 1 ms bin. I fixed it in `sleepstates.py` and added a synthetic check to the notebook that fails without the fix. The nonREM peak moved from 7.5 to 8.5 ms, still within range.
- **Code fixes:** cell 23 no longer counts pairs through `globals()`, and cell 53 no longer temporarily rebinds `sessions`.
- **Other additions:** a paired Friedman test for the burst index, a sentence on the limit of the theta-peak criterion, and updated summary and README text.

**Not done:**
- The verifier said parts of the UP/DOWN-state and autocorrelogram-decay claims could be tested with a detector or fit form chosen here. They stay blocked: that would need new criteria written before the analysis, which belongs to a new attempt.
- I made no proposed outcome changes, since this is round 1.
- I downloaded no paper text.
- I did not commit or push.

`git status` shows untracked dotfiles in the repo root (`.bashrc`, `.vscode`, `scripts` and others). I did not create them and left them alone.
