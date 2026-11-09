**Round-2 verifier report: Richardson et al. 2018 on ds000228 v1.1.1**

Cell numbers below are the current ones; they have moved since round 1.

**1. Outcomes and assumptions**

The claims file has 42 claims, and the attempt record gives 42 outcomes. I agree with 41 of them.

**I disagree on one: rc-overlap (record says partially_reproduced).** This is a change from round 1, where I agreed and missed it.
- The criterion defines only a reproduced outcome: "one overlapping timepoint is found and p <= .01 under a reading". It does not invoke Rule S and has no partial clause.
- The overlap here is 0 against the paper's 1, with a tolerance of 0 (cell 86).
- For irc-williams, the record reasons that a criterion with no partial clause can only give reproduced or not reproduced. By that same reasoning, rc-overlap is not_reproduced.
- Partial could only be defended by applying Rule S's partial clause, which this criterion does not name. The record should state that reasoning, or change the outcome.

**I agree with the other 41, including the three changed since round 1** (irc-williams, rc-child-adult-timecourse, maturity-across). For maturity-across, within-ToM is also significant under O2b+O3b (p = .049, cell 106). The record does not say so, but it does not change the outcome.

**Assumed outcomes.** Five outcomes are marked `assumed: true`: irc-tom-behavior-age, irc-fb-across, rc-fb-no-difference, rc-3yo-events and maturity-within. Each is stated in the deviations, with the outcome it would have under the other reading, and each is reasonable:
- **O2a:** the deposited regressors are one indicator per artifact timepoint (cell 8).
- **O3a:** the Methods restrict to TRs 11 to 168 only in paragraphs 9 and 13, not for the inter-region correlations.
- **O7a:** the events and their peaks are defined on the z-normalized timecourse.
- **O6b:** Methods paragraph 9 order; this one is only a tie-break.

For rc-3yo-events, the criterion asks for "the reading that reproduced rc-events", and no reading did. Using the best-matching reading is a sensible extension, and the record should say it is one.

The rule for absence claims is now stated (cell 42). The claims file has no rule for absence claims under several readings, so this fills a gap. It is not a misreading.

**Misreadings in the claims file:** I found none. I checked the voxel-size counts against Methods (paper text line 1306: n = 3 seven-year-olds and 20 aged 8 to 12), and the record's metadata_error finding is correct.

**2. Sentences the printed outputs do not support**

- **Cell 55 and the record notes for irc-adult-vs-child.** Cell 55 says "all three t values are outside 10% of -5.7, -3.8 and 7.2 under every reading", and the record says "all three t values are out of tolerance under every reading (-6.23 to -7.05, …)". Cell 54 shows within-ToM t = -6.23 under O2a+O3b, which is inside the tolerance of -5.7 ± .57. The outcome stays partial.
- **Cell 122 (Summary).** "Every behavioural and demographic number of the paper is recovered exactly from participants.tsv". Several numbers are within tolerance but not exact:
  - mean ToM scores .517 and .610 against .54 and .63 (cell 15);
  - DCCS p .048 against .049 (cell 18);
  - Inc-Fail p .015 against .01 (cell 29);
  - DCCS b .148 against .16 (cell 40).

  beh-fb-tom also holds only under reading (a).
- **Entry README.** "the inter-region correlations are higher within networks and less negative across them than the paper reports". This holds for adults, but 3-year-old within-Pain is lower: .179 against .23 (cell 62), and non-bilateral Pain .146 against .17 (cell 68). The record's first finding cites 3-year-old within-ToM (.326 against .21) and leaves out the lower 3-year-old Pain value.
- **Record notes for irc-adult.** "so the offset is in the direction of a shared signal removed in the paper's processing". This is weakly supported. The shared-signal regressor also pushes both within-network values below the paper's (.286 and .258 against .48 and .35, cell 48), so it shows only the direction of the across-network shift. Cell 49's hedged wording ("would give an offset in this direction") is acceptable.
- **README:** the run time ("about three minutes") cannot be checked from the outputs, and cell 4 says loading alone takes about two minutes.

Every other "**Result:**" sentence and every other record note I checked matches the printed numbers.

**Round-1 reasons in the record.** The record gives my round-1 reasons in my own words, with problems 1, 2, 3, 4, 5 and 7 folded into the matching claims. One detail is missing: for replication-sample I gave blocked_by data_missing, and the record does not mention that. Its response explains why `other` is used (the checker does not allow data_missing on an `elsewhere` claim), which I accept.

**3. Round-1 points**

**Resolved:**
- **Problem 3:** the absence rule is now stated (cell 42), and the four outcomes are marked assumed.
- **Problem 4:** each bin is checked against its own bound (cell 90).
- **Problem 5:** reading (b) uses 159-TR timecourses (cell 86).
- **Problem 6:** acknowledged in the verification entry.
- **Problem 7:** the ranking is shown for all 8 readings (cell 66).
- **Problem 8:** the replicated-events check is added (cells 120 and 121).
- **Mask units:** the masks are in MNI mm. Sphere centroids are within 3.7 mm of their stated centres, and M1 and V1 are exact (cell 8).
- **Image scaling:** the images are int16 with no scaling (cell 8).

**Remaining, bearing on a conclusion:**
- **Problem 1, the IRC offset.** The mean matrices and diagnostic variants are now printed (cells 47 and 48), but the offset is still unexplained. It probably drives most of the inter-region, 3-year-old and maturity failures. The record states this, as a finding and in the irc-adult notes.
- **Problem 2, the O6 tie-break.** It is now recorded as an assumption, but rc-3yo-events is still partial under O6b and not reproduced under O6a.
- **The four absence claims** (irc-tom-behavior-age, irc-fb-across, rc-fb-no-difference, maturity-within) still flip between readings. The rule is now stated, so they are decided, but their outcomes rest on the assumed readings.
- **rc-overlap:** the new disagreement above.

**Remaining, not bearing on a conclusion:** per-participant artifact counts against the ART thresholds were not recomputed, as the record says.
