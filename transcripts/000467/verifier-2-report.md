**Verifier report, round 2: Hart et al. 2023 on DANDI:000467 (0.261004.1655)**

The claims file has 32 claims. The attempt record tests 17 and blocks 15.

## 1. Outcomes

**Blocked (15).** I agree with all 15.
- 8 are blocked as data_missing: fig1cd, fig1e, the three fig1f claims, table1, fig2b-s1a and figs2cf.
- 7 are marked `data: elsewhere` in the claims file. The author kept other/not_runnable as their reasons and explained why. I accept that and drop my round-1 data_missing reason.

**Tested (17).** I agree with 15 of them:
- fig3f: not_reproduced
- fig3fg: reproduced (ratio 2.57 after the kernel fix)
- fig4b: not_reproduced
- fig4-no-decreases: not_reproduced (under the reader's rule; the placement points to motion)
- fig4-large-lasting: not_reproduced
- figs5a-sparse: reproduced
- figs5a-concentration: reproduced
- figs5b: not_reproduced
- fig6, imaging half: not_reproduced
- fig5ab: not_reproduced
- fig5d: not_reproduced
- fig5c-s6: partially_reproduced
- fig5c-6g-slow: partially_reproduced
- figs7a: not_reproduced
- figs7c: not_reproduced

I disagree with two:
- **figs5c-mho-rarely-overlaps (reproduced, assumed).** The criterion says "Reproduced when, under each M2 reading…". The four ROI-maximum readings fail: medians 1 to 3, with shared ROIs in 11 of 13 ants (cell 21). By that rule the outcome is not_reproduced. The attempt applies the same "each reading" wording literally for figs5b but not for figs5c. fig6 is not affected, since it is already not reproduced.
- **figs4a-bilateral-symmetry (partially_reproduced).** I still think this is not_reproduced. The criterion needs both parts in every ant, defines no partial outcome, and the count part fails under every reading (cell 14). This is a classification point and the disagreement is recorded.

**Assumptions (`assumed: true`).** All are stated.
- **figs5a-sparse:** reasonable. Its criterion accepts "a reading", so it hardly needs the assumption.
- **figs5a-concentration:** reasonable. 5 of the 8 readings meet it. As the notebook itself says, drawing ROIs at the higher concentration favours the subset part.
- **figs5c:** stated, but it overrides the criterion (above).
- **fig5c-s6, fig5c-6g-slow, figs7c:** the disc ROI is reasonable. These outcomes also rest on the aiiy identification, which uses the ROI maximum and drawing a. That is the reading the attempt sets aside for figs5a and figs5c. PGa comes from 4 ants (3 at 48%). The record states all this, but the inconsistency is not named.
- **fig5c-6g-slow:** the PGa part passes trivially. PGa's hexanol trace peaks at only 0.129 to 0.148, so there is no response to decline. "Partial" is fair.

## 2. Text against printed outputs

Nearly every number checks out. These do not:
- **Alarm notebook, cell 53 (Summary):** "the readings with the ROI's maximum do not [meet the criteria]". For figs5a, biix and biiy meet it (largest median 4, cell 15). The readings that fail are aiy, aiix and aiiy. The paragraph also leaves out figs5a-concentration, which the table marks "(assumed)".
- **Cell 35, and the fig5d deviation in the attempt record:** "PGa anterior and 6G lateral of PGb hold by construction". Cell 36 prints False for these:
  - "PGa anterior in all": aiiy bc, biix bd, biiy bd
  - "6G lateral in all": aiix bd, aiiy ad and bd, aiy ad and bd, biix ac, biiy ac

  The centres are re-estimated after identification, so the condition does not hold by construction. It does not change the outcome. My round-1 point 10 made the same wrong claim.
- **Cell 49, and the figs7a notes:** "One trial returns more than 100 s". Under the region ROI with return reading b, two trials do (105.9 to 110.9 s and 100.7 to 105.7 s, cell 48).
- **figs7c notes:** "All fits converged". Cell 51 prints convergence only for the coefficient-test (c) fits, not for the ML fits behind reading (a).
- **fig3fg notes:** the explanation that "ethylpyrazine's area falls more than 3-hexanone's" compares with round-1 numbers, which no current output shows.
- **README:** the runtimes "about 21 minutes" and "about 17 minutes" do not match the printed 24.6 min (alarm notebook, cell 54) and 20.2 min (concentration notebook, cell 10).

My round-1 reasons are reproduced faithfully in `verifications.results[].reason`, mostly verbatim. Where a sentence was added, it summarises my own numbered problems or notes my data_missing choice. Nothing is misattributed.

## 3. Round-1 points

**Resolved:**
1. Traces under a second identification: aiiy was added. It gives 5 of 5 ants for figs7a.
2. figs7c: the untestable case is now printed ("NOT TESTED", cell 51).
3. Stabilization: the bands are now stabilized. Against the unstabilized traces r = 0.98, and 3 of 129 trials change side of 0.2.
4. Problem 5: vehicle AL fractions are printed, with the exclusion variant.
5. Problem 6: the region ROI was run.
6. Problem 7: the Minimum filter now uses the 21-pixel kernel.
7. Problem 8: per-plane time offsets are applied.
8. Problem 9: the placement of the negative regions is checked.
9. Problem 11: the header count is fixed.

All the outputs I asked for in section C were added. Point 10 is superseded (see section 2).

**Partly resolved:**
- **Point 4 (drawing a).** Drawing a was rebuilt as the claims file describes it, now 8 to 40 ROIs per ant. But 356 of its 436 regions are still under 10 µm across (median 3.9 µm, smallest 1.3 µm; cell 9). It still mostly yields sub-glomerular fragments. That weakens the "both drawings meet it" support for figs5a, figs5a-concentration and figs5c. It also weakens the aiiy identification behind every PGa result. The claims-file issue (no size floor on drawing a) still stands.

**Remaining points that bear on a conclusion:**
- figs5c should be not_reproduced under its own "each M2 reading" criterion.
- figs4a should be not_reproduced (classification).
- The single-glomerulus outcomes (fig5c-s6, fig5c-6g-slow, figs7c) rest on aiiy. That reading uses the ROI maximum and fragment ROIs, against the ROI mean adopted elsewhere. PGa comes from 3 to 4 ants, and 8 to 9 of the 18 PGa disc traces never cross the onset bound.
- For the region ROI, 618 of 1,684 traces fell back to the disc (cell 39). The conclusions do not say so, and it softens the region-ROI comparisons in fig5c-s6, fig5c-6g-slow and figs7a.
