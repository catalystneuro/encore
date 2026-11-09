# Verifier report, round 2: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1

The claims file has 30 claims, and the attempt record has 30 outcomes: 22 reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked. Three outcomes are marked `assumed: true`: fig3h, fig4c and fig7gh. I found no place where the claims file misreads the paper.

## 1. Outcomes

I agree with 29 of the 30 outcomes. I disagree with one.

**Disagreement: fig6d-decode-p10.** The record says partially reproduced; I say not reproduced.
- The criterion requires mean forecast R − 2 s.e.m. > 0 "in each of the nine responses", and it has no partial rule. The paper's statement is specifically "in all nine".
- Cell 79 shows preparation 4, bout 1 failing under all four readings, with histories up to 100 ms, and with the code's windowing (mean R −0.060 to −0.127).
- The failure therefore does not depend on the reading. Eight of nine is a failure of exactly what the claim says, not a partial match.

**Outcomes where my round-1 view has changed**
- **fig4c (reproduced, assumed): I now agree.** The criterion judges only the mean, 10 ± 1 s, and says consistency is "reported", not judged. Under the adopted reading the mean is 10.45 s (cell 61). In round 1 I judged consistency, which the criterion does not ask for.
- **fig3h (partially reproduced, assumed): I accept it.** The criterion holds under own/le80 (18 kept and 16 returned; 19 and 17) and fails under the adopted reading (16 and 15), and the record says so. Two caveats:
  - The criterion's text gives no partial outcome. Strictly, under the adopted reading it gives not reproduced.
  - An unreported fact bears on this; see point 2 below.
- **fig7gh (partially reproduced, assumed): I agree, as I did in round 1.** The result is split by reading: one slope of two is significant under own/min80 and under own/le80 with recurrent points, and none under either pooled reading (cell 100). The same strictness caveat as fig3h applies.
- **fig7s2 (reproduced): I agree.** Cell 103 gives 0 or 1 of 10 preparations with a core, across both widths, both seeds and both participation readings. The caveat is that the ported toolbox was not checked against MATLAB, as the record says.
- **fig6s2 (reproduced): I agree.** Under own/le80 the counts are 3 to 5 and the 90% counts at least double them. The 90% models are not better: MAE p = 0.91, R² p = 0.50, with the full history grid for both (cell 83).

**Assumptions**
- All three are stated and are reasonable: the adopted reading (own/min80) follows the Methods' count rule first.
- The record openly says that fig2b fails under that same reading (by one response) and that no single reading makes the whole chain hold.
- One correction for fig7gh: the deviation says "under the pooled readings the claim is reproduced". That is true with the legend's exclusion, the main reading. With the code's exclusion, pooled/min80 has a significant total-change slope with recurrent points (p = 0.028 and 0.029, cell 100), and this is not mentioned.

## 2. Sentences the numbers do not support

- **Cell 62 and the record's fig4c notes:** "consistency holds only for the means (10.45 s against a median recurrence period of 12.73 s)". The two values differ by 2.3 s, more than twice the claim's tolerance of 1 s, so cell 61/25 does not show consistency of the means either.
- **Cell 21:** "The Methods' printed width (median ISI / 12, or / sqrt(12)) gives 22 to 76 dimensions". Cell 20 gives 21 (sqrt12/le80) to 76; the record's "21 to 76" is correct.
- **Cell 22:** "the two narrow widths give 22 to 75 dimensions". Cell 20 gives 21 to 76.
- **Cell 108, Summary:** "The Methods' kernel width as printed (median ISI / 12) gives 22 to 76 dimensions". Under /12, cell 20 gives 33 to 76; 21 to 76 is the range over both printed readings.
- **Cell 53 and the record's fig3h notes:** "The code's rule … keeps 17 to 21" is true but leaves out something that bears on the outcome. Under the adopted reading the code's rule keeps 19 periods and 18 return (0.947, cell 52). That meets both tolerances and matches the paper's 19.
- **Cell 79/83 (not discussed anywhere):** for preparation 4, bout 1 the mean MAE reaches 7.6e6 (code windowing), 6.6e7 (90%, own/min80) and 3.1e9 (90%, own/le80), which points to exploding forecasts in some windows. It does not change any outcome, since the 90% models only look worse.
- **README:** "about 36 minutes". Cell 109 prints 33.8 min, so this is trivial.
- **Record, fig7s2 entry:** it has no `notebook:` or `output:` fields, although cell 103 is tagged `claim:fig7s2-no-invariant-core`.

All other "**Result:**" sentences, the Summary's per-reading table and the README outcome table match the printed outputs.

**My round-1 reasons in the record.** They are stated faithfully in my own words. One misattribution: in fig4c, the record attaches my B.11 toy-orbit note as a reason. I had marked B.11 as not affecting a conclusion; my reasons for fig4c were the le80 failure and the missing correlation.

## 3. Round-1 points

**Resolved**
- **B.1:** disclosed in cells 21 and 22 and in the Summary table.
- **B.2:** fig7gh now runs under all four readings.
- **B.3:** fig6d now runs under all four readings and fails under every one.
- **B.4:** the "weak evidence" wording is now in fig3h and fig3i.
- **B.5 and B.6:** full history grid; own/le80 90% models; comparison on four histories.
- **B.7:** windows now count at ≥ 90%.
- **B.8:** fig7s2 is now tested.
- **B.9:** quadrant shares and true quintiles added.
- **B.10:** detrended spectrum added.
- **All items in section C:** neighbour counts, coalescence densities, the fig6d plot, the fig7gh readings, the fig6s2 equal-grid comparison and the fig7s2 outputs.

**Remaining, bearing on a conclusion**
1. **fig6d:** the outcome should be not reproduced (see section 1).
2. **fig3h:** the code's removal rule under the adopted reading meets the criterion (19 kept, 18 returned). This is unreported, and "partial" is not an outcome the criterion's text allows.
3. **fig4c:** the "consistent with" sentence is unsupported (section 2).
4. **No consistent reading:** no single reading of width and count makes fig2b, fig3h, fig4c, fig6s2 and fig7gh all hold, and fig2b fails under the adopted reading. This is now disclosed, but every assumed outcome rests on it.
5. **fig7s2:** the outcome rests on an unvalidated port of random clustering. It is stable across seeds and widths.
6. **fig7gh:** the record's statement that the pooled readings reproduce the claim depends on the exclusion rule.
