I've revised the attempt for round 1. The entry passes its checks and the clean run (`python tools/entry.py all entries/kondo-2025`, 24 minutes, no errors), and every conclusion was checked against the new numbers. Nothing is committed.

**Outcome changes**
- **fig3e-cluster-b-similar-rates: reproduced → blocked (methods_underspecified).** I agree with the verifier. Its criterion blocks the claim when the two readings of "similar" differ. For the success rate they agree in only one of the four combinations of success measure and late sessions, and round 1 had picked that one. I added a `methods_unavailable` finding asking the authors what supports "similar".
- **All other outcomes are unchanged.** They match the verifier's in all 22 claims.

**What I added or corrected, by problem**
1. **Movement onsets (problem 1):** I added a synthetic test of the onset rule. Traces with no movement get an onset before 0 in 66–85% of runs. I also added a rule requiring the crossing to last 100 ms, and the grand traces with their baseline mean and s.d. Under every rule the grand onsets stay at −0.5 s, but the traces show the jaw 6.4 px off baseline (s.d. 0.27) at −0.2 s. So in the mean the jaw moves before the pull. The claim stays blocked, and the text now says the rule was not a valid test. I put the rule to a reader in `questions/kondo-2025.yaml`.
2. **Signal degradation (problems 4 and 5):** the files hold no raw ROI fluorescence series, now shown by listing `processing/ophys` in every file.
   - The raw fluorescence is now taken from 160 frames (16 blocks of 10) instead of 8, as both median and mean.
   - Four sessions were read frame by frame. The subsample is within 1% of the all-frame median, and sampling noise is about 2% of the variance across sessions.
   - Reading (a) still finds no significant decline (rho −0.191, p 0.221).
   - Checked from the data, the blue and UV stacks fit their names. The stated `excitation_lambda` values are swapped.
3. **TTL channels (problem 2):** I added a reading of each channel over only the 19 sessions where the channel names fit the maps. Tactile and auditory give the same result as before.
4. **Auditory map (problem 3):** I added the chance level (0.61) and a shifted-onset comparison: VISa responds more at the true onsets in only 10 of 19 mice. The outcome is still reproduced, now marked as resting on little evidence, and the missing null is put to a reader.
5. **Smaller fixes and the outputs the verifier asked for:**
   - Asset kinds are now taken from the file extension (495 NWB, 1343 MP4).
   - The 16-day break is VG1-GC#85's, between task sessions 4 and 5. Without it, days per break are 2.14 ± 0.72, close to the paper's 2.3 ± 0.7.
   - The body-keypoint sessions are listed. Leaving out the two noted "face video is not available" would give the paper's 355 and 354 sessions; I state this as a possible explanation only.
   - Newly printed or counted: the lever sampling rate (5 kHz), zero T_pull values, and sessions with many extra tone TTLs. The last two are also new findings.
6. **Blocked claims:** the Google Drive folder holds only five tutorial notebooks. The Matsuzaki lab repository's dataset folder is access-restricted: anonymous listing returns "Permission denied". Both blocked claims stay `data_missing`.
7. **Record:** I recorded round 1 under `verifications`, with the verifier's reasons in its words and my response for each claim. I updated the notes, deviations and findings, and set the protocol version to `pilot-14`.

**Not done**
- The pixel-map readings for the sensory maps (fig4d) are still not run, because of the time limit. The verifier said they are not needed.
- Re-writing the record changed its line wrapping, so the diff of `attempts/kondo-2025-01.yaml` is larger than the content changes.
