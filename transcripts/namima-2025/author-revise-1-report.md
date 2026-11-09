I went through every point in the round-1 report, re-ran the entry with `python tools/entry.py all` (0 check errors, notebook passes in 296 s) and checked the conclusions against the new numbers. Nothing is committed.

**Outcome changes (2 claims, both now as the verifier gives them)**
- **ex-m1p12-no-cluster: reproduced → not_reproduced.** The claims file says an intercept is significant when its 95% interval excludes zero, and the paper says "significantly different from zero". By that rule 4 neurons count (1 positive, 3 negative), and the criterion allows at most 2. Counting only positive intercepts gives the paper's 1; the notes keep that number.
- **pop-significant-isimilarity: partially_reproduced → not_reproduced.** The criterion only says when the claim is reproduced, and no reading meets it. The notes now name dark/(a)/(ii) (394; 228 in M1, 166 in M2) as the closest reading.

**Added or corrected**
- **Reliability rule:** new output on how strict each reading of the rule is. The paper says only 2 shape and 48 texture neurons had no regression line. The half-width reading leaves 64 and 62 without one here; the width reading leaves 140 and 304, so the paper's counts favour the half-width reading. The criteria accept either reading, so I kept the outcomes. I added a question for a reader in `questions/001357.yaml`, because ex-m2p6-invariance and pop-recording-density only match under the width reading.
- **Five M1 texture files that fail the clock check:** their units respond to stimulus onset (9% to 47% fire more than on blanks, against a median of 41%) but 0% to 12% respond differently to different textures. That suggests their stimulus labels may not match the presentations, so the clock finding now says this. A variant now runs all three texture claims without these files; no texture outcome changes.
- **Noise correlations between neurons recorded together:** they are positive and largest for near pairs (0.072 within 100 µm). A new variant subtracts them, using a new helper `nc_corr_shared`, and it cuts the significant-intercept counts by about a third (dark shapes: 400 to 274). This means the counts depend on assuming independent noise, as Pospisil and Bair do. No outcome changes under the variant. I added a question for the paper's authors about it.
- **Position claims:** the check over every choice of centre position now runs under both reliability readings, and the example-penetrations test is tabulated for each fixed position label. Neither outcome changes. The minimum of 4 neurons per penetration is now explained as following from the regression-line rule.
- **Requested outputs:**
  - every column of the trial, unit and electrode tables with its description; none holds position geometry, receptive-field centres or grid coordinates;
  - a table showing that `cond_ID` 0 is exactly the presentations with no stimulus (the blanks);
  - the two-sided significance counts for M2p6 and M1p12.
- **Smaller fixes:** the helper's docstring and the deviations now say the bootstrap interval is not a confidence interval of the corrected r. The notebook's result cells, the summary and the README match the new outcomes. The runtime is updated to 5 minutes.
- **Record:** the round is recorded under `verifications` in `attempts/001357-namima-2025-01.yaml`, all 27 claims, with the verifier's reasons and my responses.

**Not done**
- **simulation-random-with-domains:** I kept `methods_underspecified` where the verifier would block it as `other`, because the reason is the parameters the paper leaves out. Both say blocked; the difference is recorded.
- **M2p9:** I did not take the dataset's p09 label as M2p9, as the verifier suggested, because a reader had already answered that the claims file's 10% rule stands. The claim fails on M2p28 whichever session is M2p9.
- **Shape outlines:** I ran no new search for a public copy of the Pasupathy and Connor shape outlines. The notes still list where the first search looked.
