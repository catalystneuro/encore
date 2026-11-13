I've finished the check of `claims/wirth-2017.yaml` and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/wirth-2017.yaml: 28 claims, 28 quotes, 25 statistical values, 0 problems` (the same before and after my edits). The file also passes the repository's schema; the only errors in a plain `yaml.safe_load` run were the `checks` dates, which both check entries share and the checker accepts.

The file had already been checked once (2026-11-10). What is new since then is that hc-12 was added as a second dataset. That turns out to matter most: the paper's Supporting data section names a single CRCNS deposit, doi 10.6080/K0R49NQV, and the descriptors show that is hc-12. hc-12 holds 189 cells, the same number the paper analyses, all in new-maze sessions. hc-21 is a later deposit (2018, 101 cells) that adds a familiar maze the paper never describes, and it also names a second paper.

**Changes, by claim**
- **Top level:** removed the `dataset: hc-21` entry. The schema says a paper's own claims file leaves it out, and with it in place the file was looked up as an hc-21-only file, so an attempt on both datasets would not have found it.
- **Every claim:** added `datasets: [crcns-hc-12]`, for the reason above.
- **Header:** rewrote the paragraph on the datasets. Also noted that the hc-12 descriptor lists the Matlab scripts the paper mentions.
- **state-space-most-responsive:** added a third way to read the chi-squared test: a goodness-of-fit test of the four counts against equal counts, which fits the paper's wording ("significantly unequal"). The pairwise tests are now given for each reading.
- **path-selectivity:** added the paper's count of one path-invariant cell to the expected values, accepted from 0 to 2 (a count of 1 cannot carry a 10% tolerance), and to the criterion.
- **direction-center-vs-periphery:** the paper does not name its test, so the criterion now marks the Wilcoxon signed-rank test as a deviation.
- **Checked, no change:** I recomputed the binomial readings in the header and they match the paper's p-values (0.0097, 0.81, 0.16 and 0.37). Every other claim checked out against the paper, and every main finding has a claim.

**Still open**
- The paper does not say whether any hc-21 new-maze sessions are its own. No claim rests on hc-21; testing on it would be a variant.
- The S1 and S2 Appendices are not under `paper/`, and reference 60 (the learning-curve method) is not named. So these stay as open as the previous check left them:
  - the methods of gaze-anticipates-action and gaze-anticipates-landmarks
  - fields-per-cell and dimensionality-control
  - the confidence bounds of the learning curves
  - the chance rate in the binomial tests of landmark-identity-distance
- I did not read the CRCNS scripts because they are files of the dataset. They might settle the map binning that the shared method leaves open.
