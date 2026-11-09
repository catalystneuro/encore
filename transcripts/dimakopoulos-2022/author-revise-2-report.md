I've finished the round-2 revision. No outcome changed, and I proposed one change for a third round. `python tools/entry.py all` passes: 0 check errors, and the notebook runs in 1585 s (26 minutes, under the 30-minute limit). A second full run gave the same numbers.

**Outcomes**
- **fig3no-p4-right-no-gc:** stays blocked (methods underspecified), as round 2 allows no changes. I proposed not_reproduced under `proposed`. The figure legends' test (a cluster test against scrambled trials) stays near its false-positive rate on shifted trial pairs of Participant 4. It found no theta cluster there, and a cluster anywhere in 4 to 20 Hz in 17% of encoding tests and 0% of maintenance tests. On the real pairing it finds significant Granger causality at all 12 right parietal contacts under each hippocampal reading. This supports the verifier's reading.
- **fig2bc-gamma-encoding-p1:** kept as partially reproduced, with the disagreement recorded. H3 rises 179%, so one of the two named contacts holds. The notes now say the regional condition tests little on this grid. I filed it as a question for a reader.
- **fig2h-gc-reversal-p1 and fig3-gc-reversal-p2-p3:** stay not reproduced. The verifier's reservation is now tested, with two added runs:
  - **Evoked responses subtracted:** the per-frequency test still flags the reversal in 20% to 50% of shifted pairs, so its excess does not come from the evoked responses. With a scrambled-trial null it still flags theta in 20% to 60% of single tests. The excess comes from testing each frequency without correction.
  - **The legends' test:** it flags the reversal in none of the shifted pairs, and on the real data it shows no reversal in Participants 1 to 3.

**Added or corrected**
- **New analyses:** a new notebook cell runs both checks above on Participants 1 to 4, using a new scrambled-trial null and an option to subtract the evoked response in `wmflow.py`.
- **Text fixes from the report:**
  - Cowan's K: 5 of 8 readings match, not four, and reading (c) is within tolerance over sessions (median 5.61).
  - fig4f: the 9 to 11 matching signs out of 29 are below chance (14.5). The d1 reading shows no reversal on correct trials either, so the paper's correct/incorrect contrast is not reproduced.
  - fig2fg: the top-six PLV contacts are now listed reading by reading.
  - "No coupling" now reads "no trial-by-trial coupling, stimulus-locked responses kept", and the "narrower than nominal" wording is gone.
  - The legend's test is now described as a cluster test against scrambled trials.
  - Run times: about 6 minutes per spatial test, and 26 minutes for the notebook (README and `entry.yaml`).
  - scalp-temporal-laplacian: the pass is now described as 1 of 36 cells at an uncorrected p = 0.02, appearing only after the reference change.
- **code_mismatch finding:** I checked it against the authors' code and it now cites lines 31 and 34 to 37 of `calculateGranger_random_trial_sampling.m` at commit 395ae13.
- **Questions for a reader:** three new ones in `questions/openneuro-ds004752.yaml`:
  - whether fig2h, fig3 and fig3no should use the legends' scrambled-trial cluster test;
  - whether the regional condition of fig2bc tests anything on this grid;
  - whether scalp-temporal-laplacian should require the sign pattern.
- **Record:** round 2 is in `verifications`, with the verifier's reasons in its own words and my responses. Its remarks not tied to a claim are under `reviewed`.

**Not done**
- The remaining spatial tests (h3, and encoding) and the per-contact h2 and h3 tests in fig2ijk. Three more spatial tests would add about 17 minutes and push the notebook past the 30-minute limit.
- The ECoG reference for sub-10 and sub-12 is still AHL4. Those subjects have no white-matter contact on another depth electrode, so it stays as documented.
- Nothing is committed, as instructed.
