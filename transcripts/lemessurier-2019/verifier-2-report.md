**Round 2 verification: LeMessurier et al. 2019 (eLife 46321) on CRCNS ssc-10**

**1. Outcomes and assumptions**

The claims file has 34 claims and the attempt record has 34 outcomes: 13 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. No outcome in the record carries `assumed: true`, so there are no assumptions to judge.

I agree with 32 outcomes. I disagree with two:

- **figs3-1-l4-nh-tuning (record says partially reproduced; I now say not reproduced).** The criterion's own partial clause needs both 0-75 µm values within tolerance and both absence tests non-significant.
  - Under E1 and E2 the eBW test is significant (p = 0.036 and 0.0051; cell 61).
  - Under E3 the test is not significant, but the L4 value is 82.1% against 73 ± 7.3.
  - So no reading meets the partial clause. figs2-1 and fig4ae fail their partial clauses in the same way and are scored not reproduced.
  - I retract my round-1 recommendation of partial for this claim. The author adopted it, so the change is my error, not theirs.
- **fig5eh-l23-correlation-gradient-at-edge (record says partially reproduced; by the criterion it is reproduced).** After the re-run every condition of the criterion holds in both responsiveness readings (cell 110):
  - EN is lower outside the column for signal and noise (p ≤ 0.0016).
  - Signal inside is not lower (p = 0.39 and 0.19).
  - The EN − NH difference is more negative outside, for noise −0.0454 against −0.0450 and −0.0430 against −0.0409.
  - My round-1 reason was that the Methods reading failed by 0.0002, which is no longer true.
  - The author's added permutation test (p = 0.96 and 0.81) is a fair caveat for the notes. But it is not in the criterion, and the claims file decides the outcome. The criterion's weakness, comparing two differences without a test, should be reported against the claims file.

The other outcomes that rest on readings or variants are stated, and each is acceptable under the "under one reading" rule:

- fig2a, fig4b and fig4d-cw rest on the stored p-values.
- fig4c rests on the raw-level variant.
- fig7c rests on pooled ensembles as units.

**2. Text checked against the printed outputs**

Almost every number in the Result conclusions, the Summary, the README and the record notes matches the outputs. These sentences do not:

- **Cell 0 and the README run time.** They say "about ten minutes" to stream and "about half an hour" (README: "about 25 minutes, ten of them streaming"). Cell 2 prints 431 s and cell 135 prints 14.1 min.
- **README, fig2a row.** "Reproduced, with the stored responsiveness p-values" leaves out the blank-median z. With the stored p and the blank-mean z only 3 of 6 values are within tolerance (cell 29). The notebook Summary (cell 136) states it correctly.
- **Summary, cell 136.** "all three put many more L2/3 NH cells … in the tuned group …, while L4 values match." That holds for E1 and E2 only: under E3 the NH L4 value is 82.1%, outside tolerance (cells 61, 67).
- **Cell 105 and the fig5a notes.** "Every value is 0.035 to 0.078 below the paper's" is true for the Methods test only. With the stored p-values the gaps go up to 0.096 (NH across-column pairs under 150 µm: 0.515 against 0.611; cell 103).
- **Record finding (responsiveness question).** "The cell counts match either" is true for L2/3 only. No reading matches the L4 counts (cell 21).
- **figs5-2 notes and cell 121.** "L2/3 response EN higher … L4 response EN lower at every weight" is right on direction, which is all the criterion asks. None of those differences is significant (L2/3 p = 0.30, 0.57, 0.93; L4 p = 0.80, 0.44, 0.73; cell 120).
  - Not disclosed: at r = 0 the responsive L2/3 count drops from 850/472 to 815/460 (cell 119), although the rebuilt traces match the stored ones.
  - `ssc10.py` gives p = 1 to ROIs with non-finite rebuilt traces, 89 of them in L2/3 (cell 6), so they are dropped as unresponsive at every weight.
  - This does not change the outcome, because the failing L2/3 part fails in the main analysis too.
- **Cell 130.** "Performance rises with ensemble size in both groups" is stated for closest-column/normalisation (a), and that is correct. Under CWs/normalisation (a) it does not rise (cell 129). That is not mentioned, and it is not needed for the outcome.

The record's verifier results state my round-1 reasons faithfully. Where the table was short, they merge in text from my problems list and section C, in my wording. One note on my own report: my round-1 totals line ("15 partially, 5 not reproduced") did not match my own table (13 and 7). The record correctly takes its counts from the table.

**3. Round-1 points**

Resolved:

- **Problem 2 (L4 neuropil).** The rebuild now filters and then subtracts and matches the stored L4 traces to within 0.012. Blanks are matched one to one at each field's own weight to within 0.013 (cell 6). The 2.29 mismatch came from three L4 fields with a shifted `sponTrace`, now handled.
- **Problem 3 (fig4c).** Raised as a question on the claims file. The outcome rests on the variant, as stated.
- **Problem 6.** A test was added. See the fig5eh disagreement above, which comes from it.
- **Problem 7.** Leave-one-mouse-out means added (Drd3-Cre EN 153.5–157.1 µm, still outside).
- **Problem 9.** `roi_probs` no longer drops training trials.
- **Section C, all items:**
  - fig2a per-bin table added (cell 30).
  - Total ROIs in C1–C3 printed (cell 21).
  - Robust slopes for figs4-1 added (cell 81).
  - Exploratory eBW counts and readings added (cell 55).
  - Not adding a blank-normalised eBW test is justified: an affine rescaling within an ROI leaves the within-ROI permutation test unchanged.

What remains that bears on a conclusion:

1. The figs3-1-l4 and fig5eh outcomes, as set out in section 1.
2. **The eBW gap (problem 1).** It is unresolved and correctly raised as a question for the authors. It still decides figs3-1-l23 (eBW part), discussion-l23, figs3-1-l4, fig3a and figs5-2 (L2/3 tuning direction). In the exploratory reading that requires each eBW to be a responsive whisker, NH comes to about 73–75%, near the paper's 67%, but EN L2/3 is still not more CW-tuned (cell 55). So fig3a does not hinge on the eBW definition.
3. **Problem 4.** fig2a, fig4b and fig4d-cw are reproduced only with the stored two-sided median p-values, which agree with the Methods test on 85.9% of ROIs. This is stated, but these outcomes are fragile.
4. **Problem 5.** For fig7c, per-field means give p = 0.024–0.42, with 0/7 sizes passing. The fig7d ANOVA treats overlapping ensembles as independent. Both are stated, and the criterion allows the pooled unit.
5. **figs2-2.** The single miss (Drd3-Cre EN) cannot be told apart from error in the radius proxy. This is stated.
6. **fig4c misreading.** The claims file's main reading (baseline-subtracted) still looks like a misreading of the Figure 4C legend. It is raised in `questions/crcns-ssc-10.yaml`, and the claim itself is unchanged.
