I worked through all 13 of the verifier's points and changed four outcomes. The entry re-ran from a clean environment with 0 errors and passed in 1336 s, and the attempt record validates against the schema. Nothing is committed.

**Outcomes that changed** (round 1, so changes are still allowed; round 2 will review them):
- **fig8-mtf-matches-filter**: partially reproduced → not reproduced, as the verifier gave it. The criterion needs a cluster in the expected region for BEFORE, AFTER and the shift between them. The shift, which carries the claim's conclusion, has none. I added a second region rule taken from the filter cutoffs, and it gives the same result.
- **supp6a-connectivity-increase**: partially reproduced → reproduced, marked as resting on an assumption. The seeds are now all 9 included electrodes, as the criterion says, and the coherence uses MNE's default multitaper setting (half-bandwidth 4, seven tapers), which is the claims file's standard choice. Frontal targets give P = 0.0039 and temporal targets P = 0.039. The temporal result fails with NW = 2 (P = 0.070) and with the paper's 6 temporal seeds (P = 0.094); the notes say so.
- **supp7-envelope-coherence**: not reproduced → reproduced, marked as resting on an assumption. At NW = 4 the temporal MIDDLE minus BEFORE test has clusters at 7.3 to 8.7 Hz (P = 0.012) and 1.3 to 2.3 Hz (P = 0.037). AFTER minus BEFORE has no cluster below 0.05, and neither do the frontal electrodes. At NW = 3 the result reverses, and this is recorded.
- **supp5b-hfb-stable-over-session**: still not reproduced, now marked as resting on an assumption. I ran all three z-scores, and the bootstrap now also resamples whole sounds or whole subjects. The slope is negative under every reading. The interval includes 0 only with the per-trial baseline z-score.

**Outcome kept despite the verifier's disagreement:** speech-r-count stays reproduced (the verifier gave partially reproduced). The criterion judges only the count, which matches; the electrode total is "reported". I recorded the disagreement and asked a reader about it.

**Added or corrected:**
- **Alignment check**, as the verifier asked: I refit the MIDDLE model with the spectrogram shifted from -0.5 to +0.5 s against the neural signal. In S01 and S04, where the models work, the best fit is within 0.1 s of no shift. In S03, S07 and S13 no shift lifts any electrode above an R2 of 0. So a misaligned stimulus does not explain the 9 against 53 electrodes.
- **New data finding**: the stimulus audio of S02, S04, S07 and S13 is not silent before the sounds start.
- **Figure 6b comparison**: our temporal and perisylvian electrode counts per subject match the paper's figure closely. The included counts per subject fall far below the paper's. Most of the paper's model scores are near or above 0, while most here are negative, which points to a different scoring. That is added to the question for the paper's authors.
- **Coherence for fig4**: now NW = 4, with NW = 2 as a variant. Windows now count only when they fall wholly inside a range. I also removed the earlier wrong statement that MNE's default gives a single taper. fig4b's 0 to 1 s window is now not significant (P = 0.17), as in the paper.
- **Smaller fixes**:
  - supp3a: the two 0.041 z means are now printed in full. They differ and come from different data, so this is not a bug.
  - PAC: an electrode is now left out of its own phase average.
  - supp4: a variant without a baseline gives the same three effects.
  - The two definitions of "frontal" are now explained in the notebook.
- **Questions for a reader** in `questions/crcns-ac-4.yaml`:
  - supp6a: the claims file says the seeds are all included electrodes, while the Supplementary Methods say temporal seeds only.
  - fig9-rms-increase: the expected 0.12 is held to an absolute tolerance, but the paper gives no unit for it.
  - speech-r-count: the total of 468 is listed as an expected value, but the criterion only reports it.
- **Records**: the round is recorded under `verifications`, three claims with `agrees: false`. The notebook text, summary and the entry README match the new numbers.

**Not done:**
- The ridge-parameter grid is unchanged. The verifier marked it as not affecting a conclusion, and it was already disclosed.
- The authors' per-subject notebooks in the dataset were read. They are a loading tutorial and fix neither the electrode selection nor the ridge parameter, so nothing changed from them.
- supp4 still starts at 3 Hz, not the claims file's 1 Hz, because the epochs are too short for a 5-cycle wavelet at 1 Hz. The variant without a baseline addresses the edge-effect concern.
- I could not run the repository's pytest tests: pytest is not installed here.
- `tools/build_site.py` was already modified before this run, and I left it alone.
