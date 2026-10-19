**Round 2 verification report: attempt 001538-zhai-2025-01 (doi:10.1126/sciadv.adv8224, DANDI 001538 version 0.260527.1302)**

**1. Outcomes**

The claims file has 45 claims and the attempt record has an outcome for each: 24 reproduced, 2 partially reproduced, 4 not reproduced and 15 blocked. I agree with all 45.

- **Changes since round 1:**
  - fig1i-dspn-dendritic-sch-lower is now not_reproduced, as I called it in round 1. P = 0.0662, exact 0.0653 (cell 50).
  - The spine claims are now blocked_by methods_underspecified, as I called them.
- **link-dendritic-cells (reproduced):** this now rests on stronger numbers.
  - Cell counts equal the paper's n in 9 of 10 groups, and the median difference is 2.9% (cell 24).
  - It is also met with the sites as labelled, so it does not depend on the new site split.
  - No claim outcome changes with or without the split (cells 47 to 86, "sites as labelled" rows).
- **fig1i-dspn-dendritic-sch-lower and fig3f-ispn-dendritic-sul-no-change (both not_reproduced):** each turns on one cell.
  - The SCH cell 20190411 cell 1 holds only its second pair of sites.
  - The sulpiride cell 20190508 cell 3 holds only a distal site.
  - Putting the paper's value for that cell back in gives exactly the paper's P in both cases: 0.0133 (cell 50) and 0.0545 (cell 66). That supports matching these cells by order, and it supports reading the gap as data missing from the dandiset, not an error in the computation.

**2. Sentences the printed outputs do not support**

- **Cell 109:** "8.5 rotations in KO against 4.25 in wild type (12 and 10 mice)". The output has 12 wild type (n_a) and 10 KO (n_b), so the counts are the wrong way round. The attempt record states it correctly ("10 and 12 mice").
- **Cell 67:** "with that value P = 0.0545, the P the paper reports, so the difference in outcome comes from that one cell." This holds for the main rule only. The same output shows the stricter basal-ratio rule gives P = 0.0663, which would also meet the criterion. The same sentence is in the fig3f-ispn-dendritic-sul-no-change notes and in the data_missing finding ("These two cells decide …").
- **Summary (cell 116):** "the stricter 0.8 to 1.25 changes the iSPN on-state result to P = 0.077". This is incomplete. The stricter rule changes two outcomes in opposite directions:
  - fig3f-ispn-dendritic-on-lower would fail (P = 0.077, cell 63);
  - fig3f-ispn-dendritic-sul-no-change would pass (P = 0.066, cell 66).
- **Attempt record, metadata_error finding:** "11 cells in such files are baseline only." Cell 5 lists 11 cells with a baseline condition in files named for a drug. Seven of them were also recorded with the drug: the 5 SCH pairs in cell 44 and the 2 sulpiride pairs in cell 60. Only 4 are baseline only (20190507 cell 1, 20190408 cell 1, 20190409 cell 1, 20190508 cell 2).
- **Attempt record, identifier_missing finding:** "the archive counts 185 subjects". No output prints this.
- **Attempt record, fig4k-confocal-spines notes:** "of the paper's 87 dendrites". No output prints this, and I did not check it against the paper.

Everything else checks out against the outputs: every other "**Result:" paragraph, the rest of the Summary, the README (its rows cover all 45 claims, and the stated run time of about ten minutes matches the 653 s printed) and the remaining notes.

- In cell 29, "peak -125 to -165 pA" is supported only by the figure from cell 28, which I viewed. The printed text gives only -165.3.

The attempt record states my round-1 reasons correctly and in my words. For fig1i-dspn-dendritic-sch-lower it records agrees: false, which is right for round 1.

**3. Round-1 points**

Resolved:
- **B1:** the SCH cell is identified, and the paper's value for it gives the paper's P.
- **B3:** three six-trial series hold two sites each and are now split. That restores the n in 9 of 10 groups, and the one remaining cell has only a distal site.
- **B4:** cell 21 now prints the order check. Each cell's best match is the row at its own rank in 8 of 12 groups.
- **B5:** one-to-one matching gives 89 exact for somatic and 5 of 11 for GRAB. No outcome changes.
- **B7:** keeping the last of a repeated step gives the same difference in 13 of 14 cells and a closer one in 1.
- **B8:** the shared cells and low power are now stated.
- **B9:** exact P is now printed.
- **B13:** the KO pairing is correct. The paper's 0.910 remains unexplained and is recorded as a paper inconsistency.
- **Section C:** every output I asked for is now in the notebook: the per-cell dendritic table, the order check, the one-to-one assignment, the AIM scores per time point, the fig7e pairing table, the Sr2+ traces and the spine file listing.

Answered with no change, not bearing on a conclusion:
- **B10:** the figure explains the 20230405b shortfall, and the per-cell amplitude reading also gives 2 of 14.
- **B6, B11 and B12:** unchanged and disclosed.

Still open, and bearing on conclusions:
- **B2, the basal-ratio rule.** The main rule (0.5 to 2) still drops none of the 165 pairs, and 38 pairs fall outside 0.8 to 1.25. The claims file fixes the 0.5 to 2 rule, so the outcomes stand under the criterion. But the two iSPN dendritic outcomes flip in opposite directions under the stricter rule. The cell 64 conclusion states this for fig3f-ispn-dendritic-on-lower. It is not stated for fig3f-ispn-dendritic-sul-no-change in the conclusion, the Summary or the finding (section 2).
- **fig1i-dspn-dendritic-sch-lower and fig3f-ispn-dendritic-sul-no-change** each rest on one cell that the dandiset holds only in part. The evidence for reading this as data missing is good (the paper's exact P is recovered in both cases), but it is still inference: no output shows the paper's sites for these two cells.
