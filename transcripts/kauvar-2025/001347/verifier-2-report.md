**1. Outcomes and assumptions**

The claims file and the attempt record both list 61 claims. The record's outcomes are 46 reproduced, 7 partially reproduced, 5 not reproduced and 3 blocked, with 14 marked `assumed: true`. The README table matches the record and the claims file on every row, for both the outcome and the data kind.

I agree with all 61 outcomes. I have reservations about these:

- **figs15, not_reproduced (assumed):** I agree. 03 c29 ran the approximate test. In the main reading ORB comes third (2.141), behind MCC (2.644) and IFG (2.267), and ORB is first in only 2 of 24 variants. The window assumption is stated and reasonable. Two caveats:
  - The deciding region, MCC, rests on 2 participants, and one of them (SD185) has a single channel.
  - The criterion takes the median over participants "as in fig. S15G". The quoted sentence comes from the S15H legend, which reports the magnitude as mean ± s.e.m. That is a misreading in the claims file. It does not change the outcome: means taken from the c29 per-participant table give MCC 2.65, IFG 2.37, ORB 2.26.
- **figs27, reproduced (assumed):** The criterion is met as written. The window and peak-threshold assumptions are stated. However, 03 c34 shows the detector is not specific to ketamine:
  - The postinfusion-against-preinfusion reference finds such channels in all 7 participants.
  - Only 2 of the 4 participants with CADSS > 10 have more channels on infusion than in that reference.
  - With 3 ketamine segments the "amplified" route cannot reach p < 0.001.

  The pass therefore does not show the oscillations are ketamine-induced. The conclusion says this. The gap is in the criterion, which has no control.
- **figs38a, not_reproduced:** I agree under the criterion's per-band weights. The outcome flips with the code's beta-weight sorting (20 of 20 readings hold). No selection reproduces the paper's 716 edges.
- **fig6e and figs37b (assumed Open C b), figs37c (assumed Open D a), figs38h (assumed pre-puff subtraction), fig1no (assumed test reading of "not above"):** The assumptions are stated and reasonable. Each one decides its outcome.
- **The other assumed outcomes** are stated and reasonable: fig2g (elbow rule), figs37a, fig5g, fig6d, fig6f, fig6h and figs34 (mouse 5 excluded, epochs, tone split).

**2. Text the printed numbers do not support**

- **03 c14, and the record's notes for link-ieeg-yeo-labels:** "reproduce the deposited Fig. 2H and Fig. 2J matrices to 6e-17". 03 c13 prints a maximum difference of 0.0 for both.
- **03 c18, and the record's notes for fig2i:** "factor 3 is (-0.041, 0.0159, model not converged)". 03 c17 prints `converged True` for the factor 3 main model. The non-converged fit is the post-hoc factor 3 post comparison.
- **03 c22:** The figs13 variant sentence ("With preinfusion loadings from all preinfusion trials … ratios 0.34 to 0.98 … 24 of 30") sits inside the fig3b method text, not in the figs13 Result. The numbers themselves are correct.
- **04 c33:** "The figure legend and the code differ on the weights, and the outcome rests on the code's reading." The not_reproduced outcome rests on the legend's per-band reading, as the heading of the same cell says.
- **04 c48 Summary, figs38a row:** "theta and alpha differ in 40 of 44 readings with per-band weights". 04 c32 prints that both differ in 18 + 20 = 38. The figure 40 is the count with at least one band differing.
- **Record notes, figs38b:** "Bonferroni (the code's pval_bonf) gives the same pattern." 04 c30 shows otherwise:
  - In the main reading, beta has BH p = 0.0266 but Bonferroni p = 0.0797.
  - In the code-band reading that meets the full criterion, beta has Bonferroni p = 0.1991 and gamma 0.1983.
- **02 c69:** "of mouse m11217 … named in the commented `extra` list of the converter". No output in 02 prints that list or links sub-5 to m11217.
- **README, "about 45 minutes in all":** the printed run times are 4.3 min (03), 2.2 min (02) and 10.7 min (04); 01 and 05 print no total. Separately, 04 c2's "about 15 to 20 minutes" is printed as 466 s in c4. Both are minor.

Everything else in the Result cells, the Summary sections, the README and the record's notes agrees with the printed outputs.

The record states my round-1 reasons in my own words: 61 results, 56 agreeing, and disagreement on fig1no, fig4b, fig6j, figs15 and figs27, as I reported.

**3. Round-1 points**

Resolved:
- 1 (fig4b, now not_reproduced)
- 3 (fig6f)
- 4 (the code's band edges are now run)
- 6 (sliding windows run; the ratio is still outside tolerance)
- 7 (fig6j now partial; tone windows run for figs34)
- 8 (fig4hi now explicit)
- 10 (fig1m code lines printed)
- 11 (figs15 and figs27 tested)
- 12 (fig6e and figs37b now assumed, with text)
- 13 (mouse 5 stated as an assumption)
- 14 (participants per factor printed)
- 15 (figs13 variant added)
- 16 (fig2g elbow assumed)
- 17 (fig1no)
- All of section C except the 716-edge selection, whose source file is not in the record.

Remaining, bearing on a conclusion:
- **fig5e (point 2):** The outcome flips with the 3–4 s code window. The claims file still does not name the two windows as readings; a question to a reader is pending.
- **figs38a and figs38b (point 5):** The paper's 716-edge selection cannot be reproduced. figs38a flips with the code's beta-weight sorting.
- **figs2bc (point 9):** The expected 0.34 conflicts with the paper's own numbers; a question is pending.
- **fig4b:** The outcome depends on whether the paper used analysis.py's max-normalisation; this is an open question for the authors.
- **figs27 (new):** The pass is not specific to ketamine (see section 1).
- **figs15 (new):** The outcome rests on approximate windows and on MCC from 2 participants. The claims file uses the median where the S15H legend gives the mean; this does not change the outcome.
- **figs38b (new):** The Bonferroni statement in the record's notes is wrong (see section 2). The outcome uses BH and does not change.
