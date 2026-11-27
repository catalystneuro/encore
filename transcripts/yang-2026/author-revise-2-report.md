No outcome changed in this round: all 25 stay as verified, 16 reproduced and 9 partially reproduced. The verifier agreed with every one and nothing is proposed. The entry's checks pass, and the full re-run passed three times; the last two runs gave the same outputs.

**One problem I found myself.** While re-running, I saw that the "drop trials without keypoints" reading (claims M5, reading b) gave different numbers on different runners.
- **Cause:** the tongue is undetected on 82% of trials, so 48 of the 278 region entries kept 7 or fewer control trials for a 7-column video regression. ses-20210129T132207, for example, kept 2. The fit was then exact, and the resulting choice axis was round-off noise.
- **Fix:** in `mam.axes`, under that reading, an entry with no more kept trials than regression columns is now left out. The notebook prints which entries, and this is recorded as a deviation under table1-early-joint-fraction.
- **Effect:** no outcome rests on that reading, so none changes. Several numbers quoted for it did change, and I updated them in the notebook and the record:
  - table1-early-axis-fractions: the drop readings give 6 of 10 within tolerance, not 7.
  - axes-cosine: the drop-reading cosines quoted in the notes (0.20 and 0.33) were stale. They are now 0.237 and 0.383.
  - fig1-1c: pooled ρ is −0.366 to −0.432 over the eight readings.
  - fig1b: the drop readings now select ses-20201230T112558 and rank the paper's session 34th of 39.

**Corrections the verifier asked for:**
- **fig1b, wrong session named:** cell 89, the notes and my round-1 response now name the session the drop readings select, and make clear that the rank belongs to the paper's session. The mismatch the verifier saw came from the runner-dependent bug above.
- **fig1e:** the highest other region is now said to be within tolerance under three of the four readings. Under reading a with independent groups it is 7.56, below 7.83.
- **fig2a:** ALM at 0.635 is now named as below 0.657, alongside thalamus.
- **fig2b:** ALM at 0.035 (50 ms steps) is now named as outside 0.036 to 0.088.
- **Run time:** the README and notebook header said about 40 minutes. They now say 35 to 60 minutes depending on the runner: the round-2 copy took 62.1 minutes and my runs about 35.

**Recorded:** round 2 is under `verifications`, with the verifier's reasons in its own words and my responses. No finding is rated critical, and the verifier agreed none should be, so the round has no `findings` items. Its review of findings 1 to 5 is summarised under `reviewed`.

**Not done:**
- **Reader questions:** none were added. The verifier reported no new place where the claims file misreads the paper, and the two open questions (fig3-1c binning, fig2d SEM rule) already stand in `questions/yang-2026.yaml`.
- **fig3c-late-residuals:** it stays reproduced at the claim's seed and flagged `seed_sensitive`. The verifier noted it is fragile but did not dispute it.
- **Next round:** the drop-reading fix was made after the verifier's review, so it has not been verified. A reviewer should check it.

Nothing is committed.
