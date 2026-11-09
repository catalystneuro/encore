I worked through every point in the round-1 report and re-ran the entry with `python tools/entry.py all`. Both notebooks pass: the main one in 25 min and `decoding.ipynb` in 34 min. `check` reports 0 errors, and every conclusion matches the executed numbers. Nothing is committed.

**Outcomes now:** 18 reproduced, 6 partially reproduced, 3 not reproduced, 5 blocked. The verifier's outcome matched the record for 26 of 32 claims. Six outcomes changed:

- **edf10b-per-animal-change** (not → reproduced) and **edf10c-environment-identity** (partially → reproduced), both marked `assumed`.
  - The paper does not say which way round a change in preferred direction is signed.
  - I now print both signs. The main reading is "earlier session minus later session". Under it, the paper's Fig. 1g means already had the paper's signs in 5 of 5 mice.
  - Applied to Extended Data Fig. 10, that rule gives 5 of 5 values within tolerance, each with the paper's sign. This holds with raw HDI too.
- **edf2-no-registration-confound** (not → reproduced).
  - The test now uses all cells regardless of CellReg score, which is what the paper means by "all cells", and corrects over 4 tests (Bonferroni), not 3.
  - Pooled over mice, both "no relation" tests are non-significant, and displacement against score is significant under both HDI readings (p 0.0011 after correction).
  - The cell count is 49 or 108, against the paper's 72.
- **edf4f-change-below-shuffle** (not → partially) and **edf9-interference** (not → partially). Both now follow the verifier: the effect is present, but no reading meets every part of the criterion.

**Added or corrected:**
- **Raw-HDI reading for every HD-cell claim.** It now covers fig2h, fig2i, fig2g, edf4ij, edf9, fig4d, edf10b/c, edf7 (the 118-cell set) and both decoder claims.
  - It changes one outcome: fig2h reaches 80% coherent under raw HDI, which meets the criterion. I kept "not reproduced" under the main reading and marked it `assumed`.
  - I rewrote the HD-cell section to say where the main reading conflicts with the paper's cell counts, and it now prints the median HD cells per session.
- **fig2g controls.**
  - A classifier given only which cell pairs are present scores 0.70, as high as the real one (0.64).
  - Splitting training and test by time within each environment's block gives 0.48.
  - The outcome stays "reproduced" because the criterion is met. The notes say the data do not show the classifier reads the correlations.
- **Decoder variant with a looser cell rule.** Test cells only need to be registered in the test session. It changes neither decoder outcome.
- **Probe-week dates (edf9).** The random protocol starts 3 days after the two-week protocol for mice 1 to 4, and 81 days after it for mouse 5.
- **Notes from the verifier:**
  - The edf1h p-values treat autocorrelated time bins as independent.
  - The edf4ef pass is fragile.
  - The fig4d means would fit if the weekly and single groups were swapped.
- **Helper bug.** A small fix in `hdstab.py`: sessions skipped while loading lacked a start date. That crashed the decoding notebook on the first full run.
- I added a sign question to the record's questions for the paper's authors. I updated the README and the runtimes in `entry.yaml`.
- Round 1 is recorded under `verifications`, with the verifier's reasons in its own words and my responses.

**Not done:**
- **edf2ab-jaccard stays "not reproduced"**, and I recorded the disagreement. The verifier would call it reproduced, because raw HDI gives 5 of 5. Choosing raw HDI for this one claim would mean picking whichever reading passes. The main reading is the one that matches the paper's session and offset counts, so I kept it for every claim.
- **fig1k stays blocked as too_large.** With four decoder fits running at once, the measured estimate is 75 min for all 1,883 fits and 47 min for the shorter partial test. Loading the circular sessions comes on top of that. Neither fits the 60-minute notebook limit with any margin. I corrected the header's old estimate to match.
- **No questions for a reader.** The verifier found no place where the claims file misreads the paper, so `questions/001676.yaml` is unchanged.
