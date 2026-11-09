I've addressed all 11 points in the round-1 report. The entry re-ran cleanly: `tools/entry.py all` passes and all three notebooks finished within the 30-minute limit (12, 20 and 16 minutes). Nothing is committed.

**Outcomes.** The record had all 18 Neuropixels claims and supp3 blocked as too_large. Each now has an outcome taken from the reviewed outputs:
- **Reproduced (14):** units per session, IC-encoder count, ed6b (assumed), ed6cd, ed2b (assumed), ed2f, ed2g, ed2a, fig2d, ed6ef, fig3a, fig3c, ed7b and ed7a.
- **Partially reproduced (1):** fig3d (assumed).
- **Not reproduced (3):** fig1e, fig1f and fig1g.
- **Blocked (22):** supp3 stays too_large, and the 21 claims on 2p data stay data_missing.

**Where I differ from the verifier (3 claims):**
- **ed2b, partially reproduced → reproduced.** The legend asks for "at least one trial in each position" and does not say standard patches only. Counting any fixed-gaze RF trial gives the paper's 9 sessions; standard trials only give 8. Under the code's reading of fig1e, 10 units remain (within 11 ± 1.1), and the orientation match beats the shuffle threshold in every combination. I adopted this as an assumption and show both rules.
- **fig2d, blocked → reproduced.** The only failure was a tie of medians (1 and 1) in one of 8 combinations. Following the protocol's tie rule, I broke it by the direction of the rank-sum test, the paper's own test. IC-encoders come out ahead in all 8 combinations, with tie-corrected p from 1e-5 to 4e-4. This is recorded as a deviation.
- **fig3d, reproduced → partially reproduced.** The second decoder setting (C chosen by inner cross-validation) now runs on every area. It gives four significant areas, with PM at p = 0.077 and AM at 0.083. The default setting (C = 1) gives five. I adopted the cross-validated setting because the paper's code also chooses hyperparameters by a search, and marked the outcome as resting on that assumption. Under neither setting does the set of significant areas match the paper's (PM significant, AM not).

**Added or corrected:**
- **Notebook split.** Decoding moved into `decoding_shin_2025.ipynb`, with both settings on all areas. It also exceeded the time limit when kept in one notebook with the main analysis.
- **Decoder checks.** These are in `decoding_checks_shin_2025.ipynb`:
  - Two further cross-validation seeds leave fig3c and fig3d unchanged.
  - Searching C up to 1000 and one-vs-all coding in V1: C above 1 never gave a higher accuracy, and the coding changed it by at most 0.024.
  - The search now allows more iterations, and non-converged fits are counted: 2 in total.
- **supp3.** The quadratic and RBF SVMs now run and agree with the linear SVM in V1, LM and AL. The network would take about 18 hours on one core, so the claim stays blocked.
- **fig1e.** Counts at each step of the selection now show where 44 and 52 units form, against the paper's 18.
- **Smaller fixes.**
  - The pupil-area maximum is now NaN for trials with no pupil fit, where it was -inf.
  - fig2d now uses the tie-corrected rank-sum test.
  - The cell text now says "21 claims", not 19.
  - The header and summary tables now match the outcomes.
- **Record.** I added the three assumptions as questions for the paper's authors, and recorded round 1 under `verifications`. There, "agrees" is judged against the record the verifier saw, so it is false for all 18 tested Neuropixels claims. Each entry gives the verifier's own outcome and reason, and my response.

**Not done.** I added no questions to `questions/000248.yaml`. The verifier's points 5 and 8 say the fig2d and fig3d criteria are brittle or loose, but neither says the claims file misreads the paper. The fig3d notes say where the significant areas differ from the statement. I also could not compare the fig1e selection with the paper's `analyzeRFCI.m` line by line, because the code was not available in this run.
