All 18 outcomes are the same as before the verifier's round. In round 1 the verifier agreed with every outcome, and the extra analyses it asked for do not move any of them. The entry was re-run with `python tools/entry.py all entries/garud-2026`: 0 check errors, the notebook passed in 418 s, and every conclusion now matches the new numbers. Nothing is committed.

**What changed in reply to the report**
- **Fig 3 on the other row set (problem 1):** I ran the value recovery on all rows off the ports as well, the set that matched Fig 2G–H. Each trial's start hex has no distance in the table, so I placed it one hex beyond the trial's next row. A > 0 in 7 of 10 rats with no minimum count and 6 of 10 with a minimum of 5, the same counts as before. Under that row set the Gaussian wins in 10 of 10 rats, or 8/1/1 with a minimum of 5, and the mean R² is still not above 0.8 for all four shapes.
- **Grid limits on the scale parameter (problem 2):**
  - **Fig 5:** λ is now searched from −5 to 5 and σ up to 10,000 hexes. A Nelder-Mead search from each optimum lowers no error by more than 1e-7, and the error of every fit is printed. Six fits with an exponential profile take a negative λ. The Gaussian CT TD model is still best summed and still wins in 8 of 10 rats.
  - **fig5d:** the measured values change from 1170.1 and 695.6 to 1201.0 and 665.0. Both are still within tolerance, though the profile value is now only about 30 above its lower limit. The first round's values are shown beside them.
  - **Fig 3 profiles:** the profiles keep a positive scale, because the paper reads A > 0 as an increase toward the goal. I widened their search range and now flag fits at a bound; the counts do not change. The very large negative A for IM-1292 is explained in the notes.
- **The ΔF/F baseline (problem 3):** I kept the claims file's baseline of ΔF/F zero. The notebook now prints each session's mean ΔF/F, which is zero by construction (median 2e-08). The notes say a late-ITI value below zero is partly forced by this, so the long-ITI result does not by itself show a tonic dip.
- **Short-ITI alignment (problem 4):** I added a cue-locked trace for every session. ΔF/F rises in the first second after the cue in 143 of 144 short-ITI sessions, which confirms the alignment.
- **Fig 2F text (problem 5):** distances 1 to 20 are now described as the 20 nearest the goal. Over the 20 distances with the most rows the r is −0.56, out of tolerance; the notes say the match depends on taking the nearest 20.
- **Fig 2A per hex position (problem 6):** averaging DA per hex position, as the Methods say, gives a mean r of −0.30 (p = 0.00057), so the ramp still holds.
- **The 9 mice without event logs (problem 7):** all 144 of their files are now opened. Each holds only photometry and TTL channels.
- **fig4b ITI reading (problem 8):** the ITI measured from reward is adopted as the best-supported reading, because its medians (7.6 s and 44.7 s) match the paper's ~8 s and ~45 s.
- **Two items the verifier could not check:**
  - `processing/` in the Floeder files holds only task parameters, so there is no depositor ΔF/F the paper could have used.
  - The Krausz et al. code (github.com/Berke-lab/DA_maze, commit 27eb743) treats `nom_rwd` as reward probability in percent, not µL as the paper says. I added this as a new finding about the paper, at the end of the list, and added the code to `inputs`. The 80/20 split is the same either way.
- **Attempt record:** the round is recorded under `verifications` in `attempts/garud-2026-01.yaml`, with the verifier's reason and my response for each claim. The notebook summary was updated to match.

**Not done**
- No questions were added to `questions/garud-2026.yaml`. The verifier did not report any place where the claims file misreads the paper.
- The supplement is still unavailable: the bioRxiv page returned "too many requests" (HTTP 429). So `figs2-no-velocity-coupling-without-goal` stays blocked (methods underspecified).
- The round's `findings` review only happens in round 2, so it has nothing to record yet.
