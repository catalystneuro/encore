**Round 2 verifier report: crcns-hc-13-yu-2017-01 (Yu et al. 2017, eLife 6:e27621)**

Counts are taken from the claims file and the attempt record. There are 32 claims and 32 outcomes: 11 reproduced, 7 partially reproduced, 11 not reproduced and 3 blocked. My round-1 totals line ("12 / 8 / 9 / 3") was wrong. My own round-1 table gives 11 / 7 / 11 / 3, and the record correctly does not copy that line.

### 1. Outcomes and assumptions

I agree with 30 of the 32 outcomes. Most are unchanged since round 1. The two that need comment:

**fig4s1b-offset-matched-coactivity (reproduced): I now agree; this changes my round-1 view.**
- The criterion for this claim does not say "under one reading". Its parent criterion, fig4b, does say "under one reading of O6 and O7", and so does every other multi-reading criterion in the claims file. So passing under O7(a) with O6(a) is a fair reading.
- My edge concern is settled by cell 82. With pinned pairs left out, the 4–5 s bin still passes (111 MAP-MAP vs 23 MAP-IAP pairs, p = 0.0004).
- It remains fragile: it passes under only one of four reading combinations. Under O7(b) there are only 8–13 MAP-IAP pairs per bin.

**fig2s1cd-theta-autocorrelation (partially reproduced): I disagree.**
- The criterion takes entry and exit from O1. The claims file's O1(b) makes every immobility period an entry or exit, and under that reading all four depth comparisons hold (cell 64), so the outcome is reproduced.
- The partial outcome rests on "well visits": immobility periods of at least 0.5 s within 15 cm of a well. The claims file has no such reading. It is the same kind of departure I refused for the no-width-rule variant in fig1s4b.
- The case that fails is a near tie: 0.00089 vs 0.00093, with 13 IAPs.
- The record should keep the claims file's reading for the outcome, and give the visit result as a variant.
- The visit definition may well be closer to the paper. The paper's "periods at wells" (Figure 1, supplement 1B–C) are visits, with peaks at 0 and 3 s for unrewarded visits. If so, that is a misreading in the claims file: O1(b) treats every pause as a well entry. It should be reported to the claims file, not fixed in the attempt. Note also that the paper's 0 s peak suggests the 0.5 s minimum excludes some real visits.

**Assumptions.** Every outcome that rests on an assumption has `assumed: true` and states it:
- The O1(b) wells, O3 speed smoothing, the Butterworth filter and the exact permutation z-scores are reasonable.
- So are the fig5s1d averaging over 100 replicates per unit, the fig4e duration weighting, and the 15 cm / 0.5 s visit definition taken as a variant.

The record contradicts itself on entries, though. In fig2c, fig2s1cd, fig2s1ij and fig4s3, the shared O1(b) deviation says "entries and exits are the starts and ends of immobility periods". The next deviation in the same outcome says they are the starts and ends of well visits.

### 2. Statements against printed outputs

Almost every number in the Result conclusions, the Summary, the README and the record's notes matches the printed outputs. These do not:

- **Cell 83, and the fig4s1b notes:** "with the +-10 s window (O7 b) only the 3 to 4 s bin is significant". That holds only under O6(a) (p = 0.014). Under O7(b) with O6(b), no bin from 1 to 5 s is significant; the 3–4 s bin gives p = 0.066 (cell 82).
- **Cell 6:** "Each day has three task sessions." Cell 5 prints 35 sessions over T1's 12 days.
- **Cell 0:** "hc-6 holds more than 28 GB over nine rats." No output supports this, and my round-1 check found about 23 GB.
- **README:** "about 14 minutes in all, 6.2 GB of memory at peak". Cell 2 prints 576 s of streaming and a peak of 6.1 GB. No total run time is printed.
- **Cell 14:** "their rate at the well falls by about half". For S2 it falls from 7.65 to 2.51 Hz, about two thirds. This is minor and does not touch the conclusion.

Everything else I checked is supported, including:
- the coverage figures (32–62%, median 53%; visits 9–37%, median 25%);
- the threshold figures (13–20% of immobile samples above threshold, 9–14% of immobile time inside events, 0.18–0.34 events/s at 3 SD);
- the edge counts (162 pairs in the last 0.5 s bin, 97 within 0.15 s of the edge; 29 MAP-IAP and 108 MAP-MAP pinned at 3.3 s);
- fig4s3 (MAP-IAP medians −0.31 to −0.06, wrong-direction p = 0.03 and 0.027);
- fig5s1d (0.394 / 0.328 / 0.495, p = 0.36 and 0.73, below 0.05 in 23 of 100 single replicates);
- the fig4a 12-day variant, and the fig5 and fig5dg sensitivity runs.

The record's round-1 reasons are my round-1 reasons, lightly edited, with nothing added. The fig4s1b disagreement is recorded with `agrees: false`.

### 3. Round-1 points

**Resolved:**
- **1, SWR threshold:** the outputs I asked for are printed. The 3 SD check leaves the fig4a, fig3c, fig5 and fig5dg outcomes as they were, so the low threshold is not what drives those failures. The question is passed on to the authors.
- **2, scope:** now stated in the header and the summary.
- **4, edge pile-up:** histograms are printed and the pinned-pair checks were run.
- **5, single shuffle in fig5s1d:** now 100 replicates per unit.
- **6, direction in fig4s3:** now printed for both comparisons.
- **7, fig4a pooled days:** a 12-day variant is added.
- **8, independence in fig6e:** now stated.
- **9, linearization:** occupancy image added, plus diagonal and minimum-occupancy variants, all null.
- **10, empty areas and LFP reference:** fixed.
- **11, no-width-rule variant:** unchanged, which is correct.
- **Section C, shared clock:** cell 13 now covers R1 and Q1.
- **Section C, spike widths:** the long R1/N2 widths still cannot be checked, because the data hold no waveforms.

**Remaining, where it bears on a conclusion:**
- **Point 3, now about procedure:** well visits, which are not a reading in the claims file, replaced O1(b) as the main definition for fig2c, fig2s1cd, fig2s1ij and fig4s3. Only fig2s1cd's outcome depends on this. It should be reproduced under the claims file's reading, and the O1(b) misreading reported to the claims file.
- **The contradictory O1(b) deviation text** in those four outcomes (section 1).
- **fig2c is reproduced, but the test is weak:** the lower notch is also above zero on the side the criterion does not test, in 94–100% of bins (cell 61). The conclusion says so.
- **The cell 83 and fig4s1b statement about O7(b)** (section 2) needs correcting. This does not change the outcome.
