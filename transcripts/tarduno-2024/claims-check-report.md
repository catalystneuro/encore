I checked the claims file for FIGSHARE:24639285 and corrected it. It is ready for an attempt.

**Checker result:** `17 claims, 17 quotes, 0 statistical values, 0 problems`. It said the same before and after my edits.

**What I checked against the paper:** all of Table 1 (24 values) and Table 2 (n, temperature range, MAD and R2 for nine specimens), the counts of failed glass specimens (22, of which 12 have no AF pre-treatment and 10 do), and the 3 of 25 success rate. All the recorded numbers are right.

**Changes, by claim:**
- **Five crystal claims** (table1-max-intensity, fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent, crystal-14053g1-400c-stable): the source said "Results, Single crystal measurements". The paper has no Results section; that subsection sits under Background & Summary. I changed the sources and the opening comment.
- **baseline-range:** the quoted sentence is in Background & Summary paragraph 7, not 6.
- **interpretation-impact-no-dynamo:** the source now points to the Abstract and Background & Summary paragraphs 2 and 7. Paragraph 6 is about the replicate measurements.
- **table2-fit-statistics:** the statement claimed the listed failure criteria "follow from" the values. The paper doesn't say that, and the criterion doesn't test it, so I removed it.
- **table2-no-fit:** the criterion now says the pTRM check comparison is only reported and does not decide the outcome. It had no expected values or rule.
- **crystal-14053g1-400c-stable:** the existing reading compares replicate 400 C directions, but there may be only one 400 C measurement. I added a second reading: the 400 C direction lies within the alpha95 of the mean NRM replicate direction.
- **no-alteration-recording-efficiency:** reading (b) said "about twice" with no cutoff. It now uses a ratio above 2 as failing, marked as a choice not taken from the paper.
- **Opening comment:** Table 1's max intensities are 0 to 3% above what the formula gives from its own M590 column, not 1 to 3%. 12053g2 is 0.2% below.

**Still open (recorded in the check entry):**
- For glass-directions-not-random and glass-af-no-change the paper names no test or threshold. The readings in those criteria are labelled as not from the paper.
- The definitions of M590, MAD and the pTRM check percentage remain open. The possible readings are listed in the opening comment.
- Table 1 gives the same M590 value (6.292E-09) for 12021g3 and 12040g3, which may be a copying error in the paper.
- No PDF was supplied, so the nominal paleointensities and arrow ranges in Figures 1 and 2 are not recorded.

**Ready:** yes. The check entry is at the end of the file with `ready: true`. Nothing is committed.
