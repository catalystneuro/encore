**Round 2 verification: Zhai et al. 2025 (doi:10.1126/sciadv.adv8224) on DANDI:001538 draft**

The claims file has 45 claims. The attempt record has 45 outcomes, one per claim: 34 reproduced, 2 partially reproduced, 2 not reproduced and 7 blocked (the 6 spine claims and fig8bc). So 38 claims are tested. My round-1 count of "39 tested, 6 blocked" was wrong; fig8bc was blocked then too.

**1. Outcomes and assumptions**

I agree with all 45 stated outcomes.

Six outcomes carry `assumed: true`, and each assumption is stated in the record's deviations:

- **link-sr-cells, fig2h, fig2i, fig4g, fig4h (the event detector).** Stated and reasonable. The paper gives no TaroTools settings. Each outcome now also holds on the paper's own per-cell values, run next to the detector results (cells 81, 84, 87, 90: P = 0.0003, 0.130, 0.0003, 0.23).
- **fig1i-dspn-dendritic-sch-lower (2019-04-11 cell 1 left out; changed from not_reproduced to reproduced).** Stated and reasonable.
  - The dandiset description says the first site pair of this cell is not deposited.
  - The left-out paper value (0.228) is the lowest in the SCH group, so it is the value that most supports the claim. Removing it works against reproduction.
  - The paper's own table without that row gives U = 65, P = 0.027, the same as the dandiset without the cell (cell 64).
  - The outcome now rests on 8 SCH cells where the paper used 9. With the cell, P = 0.066. Both facts are stated.

**2. Sentences the printed numbers do not support**

- **Cell 65, the attempt record's notes and its round-1 response for fig1i-dspn-dendritic-sch-lower:** "the other eight SCH cells are within 10% of the paper's rows."
  - Cell 20 gives 0.778 within 10% for the SCH group, which is 7 of 9.
  - Cell 64 shows 2019-05-03 cell 3 at 0.289 against the paper's 0.261, a difference of 10.7%.
  - The correct statement is 7 of the other 8. This does not change the outcome.
- **Entry README:** "It takes about eight minutes." Cell 138 prints a total run time of 13.1 min. Loading alone takes about 11 min in cell 3 (306 + 43 + 135 + 193 s).
- **Attempt record, fig2h deviation:** "The reading the paper best supports is adopted: 5 SD … and the per-cell median." The notes and cell 82 lead with the per-cell mean (P = 0.0031) and give the median second (P = 0.0044). Both are below 0.05, so the outcome stands, but the adopted reading and the headline number disagree.
- **Cell 27:** it lists the missing background images as a possible cause of the gaps, then says in the same parenthesis that "they cancel in the normalised area". If they cancel, they cannot explain the gaps. The sentence is self-contradictory but does not affect the outcome.

All other "**Result:**" cells, the Summary, the README rows and the record's notes agree with the printed outputs. The README's group counts (3, 5, 5, 8 and 6 claims) add up to 45.

The record's verification block gives my round-1 reasons faithfully, paraphrased closely from my report. One thing is carried over from me: the fig4k reason repeats my round-1 count of "17 Adora2Cre M#### files". Cell 14 counts 16 confocal Z-stacks plus 1 overview, so my figure was off by one. Round-1 problem 7 (how the Sr2+ files were picked) is in no reason, as it belonged to no single claim. It is resolved.

**3. Round-1 points**

All nine are resolved:

1. **Confocal images:** cell 14 counts 16 Z-stacks naming Figure 4, J and K, and the Figure 4I overview. The blocked reason is corrected.
2. **Spine blocks:** they now use the reason methods_underspecified, the 76 two-photon files are counted, and a finding asks the authors about the manual correction.
3. **SCH dendritic data gap:** cell 64 adds the per-cell comparison and the tests with and without the cell. The outcome is changed with a stated assumption, as discussed above.
4. **Frequency claims and the detector:** the tests on the paper's own frequencies are added, and both absences hold on them.
5. **Mean against median amplitude:** handled. Cell 24 shows the result under both readings, and a question asks a reader whether the criterion should compare the median. The claims file's misreading is reported, not corrected.
6. **GRAB matching:** the TTX-only and quinpirole Fmin rules are added, each matched many-to-one and one-to-one. The Methods' rule matches best, and the outcome is not reproduced under every reading.
7. **Sr2+ file selection:** cell 3 now picks the files by session description, and cell 13 prints the check.
8. **Last-sweep variant:** run for every somatic claim, with the same outcomes.
9. **AIM merge:** sessions are now merged on figure, mouse and session, and no mouse number repeats across the two figures.

My round-1 "could not check" items are also settled:
- The condition column agrees with the session names and subject folders (cell 13).
- The lab's own total column gives F = 29.30, equal to the paper's (cell 110).

**What remains that bears on a conclusion:** only the fig1i-dspn-dendritic-sch-lower outcome. It is reproduced only if 2019-04-11 cell 1 is left out; with that cell, P = 0.066. I find the assumption reasonable. Its supporting sentence needs correcting from "the other eight cells within 10%" to 7 of 8. The other items in section 2 are wording fixes.
