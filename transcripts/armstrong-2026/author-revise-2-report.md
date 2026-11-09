The verifier agreed with all 33 outcomes in round 2. No outcome changed and none is proposed. The final re-run with `python tools/entry.py all entries/001341-armstrong-2026` passed: 0 check errors, notebook ran in 335 s, and the key numbers came out the same as in the first re-run.

**Text corrected to match the printed outputs**
- **Cell 17:** for 489, the largest bin in the ramp window is now compared with the largest elsewhere: 8.01 against 8.69 Hz for left turns (OL_L), 7.46 against 8.32 Hz for right turns (OL_R). It also says that for 503 right turns, the 10.78 Hz ramp-window peak is the highest bin over -1 to 2 s.
- **Cell 22, animal 489:**
  - "Nothing beyond chance" is replaced. The text now says the best lags of windows 0 to 6 rise almost steadily (4.36 to 12.23 s), and the first two speed windows agree with them.
  - It still says no window's lag is separated from chance and no clock can be fitted.
- **Cell 22, animal 503:**
  - The two swapped 95th percentiles (0.552 and 0.535) are fixed.
  - The onset lags of all seven windows are now compared with the speed clock. Window 3 is 3.2 s off, and windows 0 and 4 to 6 are 2.7 to 36.3 s off.
  - A caveat is added: the clock was fitted to running speed, and 503 runs in 1.7% of left turns against 31.8% of right turns. So the turn-specific responses and the decoding on that clock may partly reflect running, and so may the 0.655 before the onset.
- **Cell 28:** the rate at the stored onsets now reads 7.15 to 7.48 Hz.
- **Cell 43, the DDM fit (fig4-ddm-fit):**
  - The mixture weight is at its 0.1 limit only in the 16 DDM fits. With a 0.3 limit it is 0.158 to 0.243, which is below that limit but well above the 3 to 5% of reaction times under 0.1 s. That points to the plain DDM misfitting the shape of the reaction-time distribution more broadly.
  - A nondecision time of 0.12 s is now called "narrowly excluded" by the likelihood profile (p about 0.04), not "not excluded".
  - With the 0.1 s cutoff, only two of the four fits have the leak near the +10 edge.
- **Cell 44, the summary, the README and the record's notes and findings:** the same corrections for 489 and the running caveat for 503 are carried through.
- **fig4-ddm-fit notes in the record:** these now say plainly that the partial outcome rests on the assumption about early reaction times. Under the mixture handling the GDDM condition also fails, so the claim would be not reproduced. Confidence is stated as low.

**Record**
- The round-1 entry wrongly said the claims-file header had been changed to note the paper's TTL synchronisation. It had not been changed, since the author does not edit the claims file, and the entry now says so. The TTL point stays in the notes and findings.
- The repeated "Kept blocked." in the round-1 responses for fig1jk-all-units and fig5b-epochs-in-subpopulations is removed.
- Round 2 is recorded under `verifications` for all 33 claims, with the verifier's reasons and my responses.

**Not done**
- I added nothing to `questions/001341.yaml`. The verifier found no misreading of the paper, and the header note is a suggestion, not a misreading.
- I fitted no clock for 489. The verifier agreed this changes no outcome, since such a clock would be no finer than the one for 503.
- `tools/build_site.py` was already modified before this run started. I did not touch it.
