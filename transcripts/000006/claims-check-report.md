I checked the claims file for 000006 and made 15 corrections; I judge it ready for an attempt. To check the criteria that cite the paper's code, I downloaded the paper's electrophysiology zip from Figshare (doi:10.25378/janelia.7007846, v1), the same source the original reader used. I unpacked only the MATLAB `.m` files and opened no data. Nothing was committed or pushed.

**Checker result:** `31 claims, 31 quotes, 10 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim**
- **Opening comment:** added two details from the code.
  - A neuron's coding-direction weight is set to 0 when its rank-sum p is 1.
  - Epoch means use time > start and ≤ end, unlike the coding-direction windows.
- **pt-types-transcriptomic, pt-types-account-for-all-pt:** the statements said more than the paper. The paper only "suggests" the data divide PT neurons into two types; the wording now matches.
- **pt-projection-cluster-mapping:** source was paragraphs 4 and 5; both counts are in paragraph 4.
- **pt-depth:** the code plots each unit's own depth field, not the session manipulator reading it also stores. Both are now readings.
- **pt-lower-heterogeneous-rates:** "χ2 test" names no specific two-sample test. Bartlett's test and the code's F test are now both readings, and the outcome is the one they both give; before, Bartlett was the main test and the F test only a variant.
- **pt-upper-early-preparatory:** the extra rule for "larger" (PTupper 5th percentile above the PTlower median) is not in the paper. It is now one of two named readings, the other being a plain comparison of medians.
- **pt-single-neuron-early-selectivity:** the criterion accepted p < 0.01 under either test. The test is an open method detail, so both tests must now agree.
- **pt-upper-decoding, pt-upper-decoding-rectified:**
  - The code does not cut at a fixed 70% accuracy. It counts units above the mean + 1 s.d. of all PT accuracies, so that cut is added as a reading.
  - I removed the `statistic` field, which held group means, not a test statistic.
- **pt-variance-explained:** added two code variants: every neuron's trials are resampled in each iteration, and variance explained is taken per neuron and then averaged.
- **pt-cdgo-onset:** "before the first detectable movement" is not in the paper. It now reads "consistent with a role in movement initiation", from the Fig. 6c legend.
- **reaction-time:** the claim is now judged on the paper's own 99% interval (38 to 56 ms), not a 10% tolerance; the expected tolerance is 6 ms.
- **pt-cohort-control:** noted that the Extended Data Fig. 8 legend says "contralateral" where the Methods say right ALM; the Methods are followed.
- **pt-lower-late-and-motor, pt-types-differ-in-timing:** the Discussion paragraph was wrong; corrected to paragraphs 1 and 3.

**What remains open**
- Some judging rules come from the first reader, not the paper, and are named as readings:
  - the ratio bound of 1.3 in pt-variance-explained, taken from the figure's axis range;
  - the 0.5 and 0.75 levels and the 0.2 s bound in pt-cd-change-at-go-cue;
  - the windows in pt-lower-movement-termination;
  - the "similar" rule in pt-cohort-control;
  - "more consistent across trials" in pt-upper-early-preparatory.
- I could not check paragraph numbers in the "Cell-type-specific recordings" section against the PDF, because no PDF renderer is available here. The quotes still locate each finding.
- Every main finding has a claim, and all claims come from this paper.

**Ready:** yes. The entry is under `checks` with `ready: true`, and the file still passes the checker.
