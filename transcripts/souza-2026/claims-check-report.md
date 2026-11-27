I've reviewed `claims/souza-2026.yaml`, fixed what I could show was wrong from the paper, and added a check entry with `ready: true`. Nothing is committed.

**Checker:** `claims/souza-2026.yaml: 38 claims, 38 quotes, 13 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

**Changes, by claim**
- **fig1d-split-half-above-null:** the rule "cohort median above the null's 95th percentile" was not from the paper. The paper gives no measure for "well above", so the criterion now names this as open, with two readings, and marks the outcome as resting on the one used.
- **fig1gi-waveform-separation, fig1m-narrow-stronger-m:** a Mann-Whitney test the paper never reports was deciding the outcome. Both claims are now judged on the ordering of medians, which is what the paper states, and the test is kept only as a variant.
- **fig1h-median-isi-narrow-broad:** the legend's counts (2,308 + 8,716 = 11,024) don't fit the 10,805 cohort units left once the 227 ambiguous ones are removed. I named the class counts as open, with two readings.
- **waveform-ambiguous-band:** the file said the 53,806 units are "units with a waveform". The paper doesn't say why only 53,806 enter, so this is now stated as an assumption.
- **layer4-suppression:** the criterion also accepted +0.148 in place of the reported +0.116. It is now judged on +0.116 only.
- **layer4-controls:** +0.148, which is the unmatched figure in the firing-rate-matching control, is now an expected value here. The paper leaves the gap between +0.148 and +0.116 unexplained, and the criterion names that as open.
- **m-baseline-sensitivity:** its source paragraph number disagreed with fig1mn's for the same sentence. I corrected it and added the paragraph's opening words so it can be found.
- **fig2d-cv-correlations:** the criterion took the false-discovery-rate p values from 1,000 permutations, which can't go below about 1e-3, so they can't produce the reported 1.0e-12. They are now read as parametric Pearson p values, corrected across the 66 pairs.
- **layer-assignment-coverage:** the VISam and VISrl expected values were labelled as cohort percentages, but the criterion says cohort or all units is open. The labels now match the criterion.
- **hits-vs-false-alarms:** "102 sessions with false alarms" is now "102 sessions covered by this family", as the paper says.

**What remains open**
- Paragraph numbers in Methods 2.5 and Results 3.2 can't be confirmed, because the text extraction loses paragraph breaks and there is no PDF. The quotes still locate each finding.
- The paper doesn't describe two methods: the firing-rate matching across layers, and the pre- and post-stimulus windows of Figure 2F. The readings in those criteria are the file's own, taken from the nearest Methods passages.
- No analysis code is available (the paper offers it "upon reasonable request"), so none of these open details can be settled from code.

**Coverage:** every main finding in the abstract and Results has a claim. Every claim comes from this paper.

**Ready:** yes. The file is fit for an attempt.
