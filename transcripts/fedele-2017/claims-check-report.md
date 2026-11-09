The file is ready for an attempt. The checker's result, before and after my edits: `claims/fedele-2017.yaml: 20 claims, 18 quotes, 19 statistical values, 0 problems`.

**What holds up.** I recomputed these from the paper's own tables and they all match:
- **Table 2:** every percentage follows from the Table 1 columns. The ripple and FR counts (7/4 and 9/5) are right.
- **Follow-up:** means 29.3 and 22.8 months, SDs 15.3 and 10.7, ranksum p of 0.25 under every test variant.
- **Chi2 p-values:** the ones the criteria give are right (0.0023 for the main result; 0.0001, 0.0012 and 0.0010 for the Engel version).
- **Confidence intervals:** every printed interval except one is the Clopper-Pearson interval.
- **Test-retest:** the medians and lower quartiles follow from Table 1 using Matlab's `prctile` (0.975 and 0.67; 1 and 1), as do the group medians (0.985, 0.97, 0.36).

No claim comes from outside this paper, the main findings are all covered, and no part of a method is made up without being named as open.

**Changes, by claim:**
- **Opening comment:** added an inconsistency the file missed. The Methods allow at most six intervals per night, but Table 1 gives seven patients more than that (for example patient 3: 5 nights, 39 intervals).
- **cohort:** the source now says where the 41–85% CI is printed, since the quote doesn't contain it.
- **table1-nights-intervals:** the criterion notes that inconsistency and compares with Table 1 as printed.
- **followup-not-different:** the criterion now records that both test variants give p = 0.25.
- **table2-frandr-prediction:** added the p-values for the other two test readings (Yates 0.014, Fisher 0.0072).
- **ete-soz-not-resected:** neither the paper nor the data description lists seizure onset zone (SOZ) channels, so the criterion now says the SOZ part can't be tested in that case.
- **test-retest-by-group:** added the Table 1 legend to the source.
- **spectral-classes:** "second peak" is now named as open, with two readings. The Results call it the second peak; the Discussion describes 240 Hz as a prominent peak "around 200 Hz".

**Still open:**
- The Results print a specificity CI of 78–100%, which no standard method gives. Clopper-Pearson gives 75.3–100%, which the Discussion prints as 75–100%.
- The SOZ parts of ete-soz-not-resected and fig2-patient17 can't be tested unless the dataset marks SOZ channels.

The `checks` entry has `ready: true`. Nothing was committed.
