**Round 2 verification: Lee et al. 2025 (eLife 105955) on DANDI:001195**

The claims file has 38 claims, and the attempt record has 38 outcomes. Twelve were tested: 5 reproduced, 6 partially reproduced and 1 not reproduced. The other 26 are blocked: 1 for insufficient metadata, 25 for missing data. Two outcomes carry `assumed: true`: fig6k and fig7-s1ef.

## 1. Outcomes and assumptions

| Claim | Record | Do I agree? |
|---|---|---|
| fig6df | reproduced | Yes. The criterion's own test also passes on the light-free window (cell 15), and the record says so. The support is the contrast between light and no light. For IPSPs that contrast is weak at 3 SD (53.2% against 30.3%) and clear only at 4 SD and above. |
| fig6gi | partially | Yes. |
| fig6j | partially | Yes, but the notes leave out a fact that bears on it. The only criterion reading that passes, (a) at 3 SD with p = 0.049, fails when the one cell with an evoked action potential (C15) is dropped: p = 0.075, Dunn p = 0.071 (cell 21, second table). Neither the notes nor cell 22 mention this. The support comes from the 5 SD variant and the male-only variant. |
| fig6k (assumed) | partially | Yes, but the reason given for the assumption does not hold. The record says 2 SD is rejected because "most detected IPSPs are noise" (67% false detections without light against 82.6% with light). The same arithmetic applies at 3 SD: 30.3% without light against 53.2% with light, so more than half of the 3 SD IPSPs could also be noise. Only 5 SD separates signal from noise (4.6% against 19.3%), and there the CeA trough is also deeper, though BNST has 1 cell, so only two regions are compared. The assumption is stated; its justification should rest on the agreement between 3 SD and 5 SD. |
| fig6-s1de | blocked (metadata_insufficient) | Yes (cell 6). |
| fig6no | partially | No, I keep not reproduced. The criterion has no partial clause. In every reading the late-firing cluster has 2–3 inhibited cells, and the readings agree (cell 31). |
| fig6-s1h | reproduced | Yes (cell 34). |
| fig6pq | partially | Yes, on the criterion's 2 and 3 SD readings. At 5 SD the direction fails: 41.2% of the pyramidal cluster are inhibited and 52.9% excited (cell 37). The notes give the 41.2% but do not say the direction fails. |
| fig6-s1i | reproduced | Yes (cell 40). |
| fig6-s1jk | reproduced | Yes on all cells. With male mice only it fails at every k (cell 56). Keeping the cells labelled female goes against the paper's Methods, which use male mice only, and this outcome turns on that choice. It should be marked `assumed: true`. |
| fig6-s1ln | not reproduced | Yes. |
| fig7-s1ef (assumed) | reproduced | Yes. The assumption that the blue sweeps carry blue light only is stated and reasonable. The per-cell data support it more than the record says: in cells C4 and C9 of subject 235, red light during constant blue gives 16.1 and 11.9 mV, while the "blue" sweeps give under 1.2 mV (cells 49 and 52). So in those cells the blue sweeps cannot be red pulses under blue light. |
| fig7-s1hi | partially | Yes. Detection "in 13 of 13" at 2 and 3 SD is uninformative given the false-detection rate; at 5 SD it is 10 of 13. |
| 25 blocked (data missing) | blocked | Yes. |

## 2. Statements the printed numbers do not support

- **Attempt record, fig6-s1jk notes:** "With the mice labelled male only the BLP area and EPSP tests are not significant." Cell 56 prints only "k=2: False; k=3: False; k=5: False", so which tests fail is not shown.
- **Cell 41 and the fig6-s1i notes:** "in a version of this analysis that left out P10, the clusters had 12 and 15 cells and the delay no longer differed." No output shows this, and the text says that version is not run. Since it bears on whether this outcome is robust, it should be run or the sentence removed.
- **Cell 13:** "Its other sweeps (34 at rest, …) are normal and are kept." Cell 7 gives P10 79 rest sweeps, and all 51 failed sweeps are rest sweeps (P10's firing sweeps are at 62–86 pA). That leaves 28 valid rest sweeps, 26 after removing the 2 that fire before the light.
- **Cell 27 and the deviations of fig6pq, fig6-s1i and fig6-s1ln:** capacitance reads low "by about the same factor in every cell." Nothing is printed that shows this. Without series and membrane resistance correction, the error depends on each cell's own resistances.
- **Cell 57:** "the combined clustering does not show the pattern of Figure 6 supplement 1N in every reading." This is true but misleading. The printed flag is an all-readings test that includes k = 5, which fails even with all cells. Whether the pattern holds at 2 and 3 SD with male mice only is not shown.
- **Cell 13:** "The sex in the files, or the paper's statement, is wrong for these cells." This leaves out a third possibility: the female-labelled cells are not in the paper. The male-only rest count for BLP is exactly the paper's 48 (cell 15), which points that way.

Every other sentence I checked against the outputs matches. That covers the remaining "Result:" cells (16, 19, 22, 25, 32, 35, 38, 44, 47, 50, 53), the Summary, the README and the record's notes and findings.

My round-1 reasons appear in the record word for word, apart from ASCII changes (± to +-, en dashes to hyphens, ≤ to <=). So they are in my own words.

## 3. Round-1 points

**Resolved:**
- **Problem 3, spiking rest sweeps:** sweeps that fire before the light are now left out, and the holding-current mismatches are tabulated.
- **Problem 4, P10:** its failed sweeps are left out.
- **Problem 5, blue sweeps:** the assumption is stated and the light-onset check is run on the ChrimsonR sweeps.
- **Problem 6, B7 and the spike threshold:** handled.
- **Problem 8, TTX search:** the wider search is run and the markdown corrected.
- **Problem 10, imaging metadata:** now in the findings.
- From my list of things I could not check: per-cell late-cluster table, sweep table, onset check, file text fields, video frames. All done.

**Partly resolved, still bearing on a conclusion:**
- **Problem 1, detection in noise.** It is now measured, and 5 SD labels are shown. But the conclusions still rest on 2 and 3 SD, which the data show are largely noise for IPSPs. At 5 SD:
  - the fig6pq direction fails;
  - the fig6-s1ln pattern of Figure 6 supplement 1N fails;
  - fig6j passes;
  - fig6no's regular-firing condition fails (3 of 9–10 inhibited).

  The fig6k assumption needs the corrected reason given above.
- **Problem 2, sex.** It is now reported and the male-only variant is run. fig6-s1jk is reproduced only with the female-labelled cells and should be marked as resting on that assumption. The record should also say which of its tests fail with male mice only.
- **fig6j fragility (new, from problem 3).** C15's evoked action potential decides the one passing criterion reading. This should go in the notes.
- **Problem 9, the claims file's fig6-s1ln condition.** This is the claims file possibly misreading the paper, and it is reported, not corrected. It is still open and has been sent to a reader. I still cannot render the figures here, so I could not check Figure 6 supplement 1N or the pies of Figure 6O. On the pies: the claims file says they include cells with no response, yet fig6no requires every late-firing cell to be excited. That outcome fails on its inhibited cells either way.

**Not affecting a conclusion:**
- **Problem 7, capacitance:** stated as a deviation, with the overstatement listed in section 2.
- **fig6-s1i:** the P10-removed statement should be run or removed.
- **fig7i:** CellReg co-registration was not run; the record states this and gives a reason.
