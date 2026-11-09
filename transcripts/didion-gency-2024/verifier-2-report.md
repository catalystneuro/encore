**Verifier report, round 2: Didion-Gency et al. (2024), DRYAD:4j0zpc8hz v260590**

**1. Outcomes**

The claims file has 39 claims, and the attempt record gives an outcome for each:

| Outcome | Count |
|---|---|
| Reproduced | 14 |
| Partially reproduced | 3 |
| Not reproduced | 7 |
| Blocked, methods underspecified | 10 |
| Blocked, data missing | 5 |

Every outcome matches the re-executed notebook's printed outputs, and I agree with all 39.

The one change since round 1 is **tables3-oak-wmr-diameter**, from reproduced to blocked (methods_underspecified). I agree with it:
- Cell 116: it passes only under Y1/S3/A1, with +1.38 and p 0.023.
- Under A2 that contrast has p 0.16.
- Over all rows the difference is +1.69 under every reading, outside 1.4 ± 0.14.
- The claims file asks for "Tukey-type" contrasts, which argues against A1 (no adjustment). So the claim could not be reproduced unless the A1 and S3-row choices are both settled in its favour.

Two outcomes rest on reading P1 alone; I accept both because the claims file allows P1:
- **fig1cd-development-duration**: with a random intercept per treatment and year, oak has p 0.11 (cell 18).
- **fig1-oak-steeper-advance**: the same variant gives p 0.097 (cell 27).

**2. Text checked against the printed outputs**

Every "**Result:**" cell (16 to 120) matches its outputs in values and ranges. These sentences do not:

- **Attempt record, fig4-wmr-same-as-mr notes:** "Largest absolute raw differences per trait are … 0.50 to 2.39 in oak." Cell 75 gives oak Photo "1.13 to 2.86", so the range is 0.50 to 2.86.
- **README and Summary (cell 123):** "reproduces Supplemental Table S1 for some traits exactly". Cell 10 shows only oak AGWB as exact (0.00). The next closest are oak midday at 0.02, beech AGWB at 0.21 and beech Asat at 0.25. The attempt record's own finding says this correctly ("for oak AGWB increment exactly and for beech Asat within 0.25").
- **Cell 105:** "beech diameter increment is not lower in mixtures under any reading". On the rows S3 keeps it is lower (−0.17 in 2021 and −0.22 over both years, cell 104), just not significantly. It should say "not significantly lower".
- **Cell 4 (data check, not a conclusion):** "35 rows repeat another row exactly (trees 17, 35 and 45)". Cell 3 prints trees [17, 35, 45, 144].
- **Attempt record, `verifications.reviewed`:** it says B9, including "the pre-treatment 2019 campaign under T1", is "recorded as findings or deviations". Nothing in the record mentions the pre-treatment campaign.

The attempt record states my round-1 reasons accurately and in my own wording. The general points (B1, B4, B7, B8) are folded into the per-claim reasons, and nothing is misattributed.

**3. Round-1 points**

Resolved:
- **B1 and B2:** reading A2 (adjusted contrasts) and the difference over all rows (`raw_all`) were added. tables3-oak-wmr-diameter is now blocked, and no other outcome changes under A2.
- **B6:** the Table S6 F values are now compared with the paper's. The closest readings are y2, monocultures, both species pooled, marginal tests, under S2 and S1, with largest differences 0.99 and 1.01. That is the reading under which the absence holds, but it is not a match, so blocked stands.
- **B8:** the P1 variant with a random intercept per treatment and year was added, and the notes now say which results rest on P1.
- **B11:** cell 0 now lists only which claims are tested.
- **B3 (partly):** the Metadata and README-sheet descriptions are now printed; neither defines Growth_length.
- **B5, B7, B9 and B10** need no change to any outcome.

Still open, and bearing on a conclusion:
- **B3, fig1ij-growing-season and reading (b) of fig1-oak-steeper-advance:** the outcome uses the deposited Growth_length. On the definition the criterion gives (bud swelling to onset of senescence), beech has slope 1.09 with p 0.085, and the claim fails (cell 24). This waits on the question that was asked.
- **B4, the claims file's reading of Eqs. 3 and 4 (a claims-file misreading, still unanswered):** this reading makes CE exactly 2 × NBE, so the complementarity part of fig5-beech-sugar-nbe-mr, fig5-oak-agwb-nbe-warming-2020 and fig5-oak-asat-nbe-wmr-2021 is not tested on its own. It also makes SE 0 under B1/L1 in figs2-beech-asat-selection-warming. The reading is also internally inconsistent: NBE ≠ CE + SE. For example, in cell 119 under B2/L2 in 2021, NBE is +194, CE +388 and SE −275 (p 0.0039).
- **B1, A1 against A2:** this still decides tables3-oak-wmr-diameter, together with which rows the S3 difference is taken over. Both are now in a question.
- **B8:** fig1cd-development-duration (oak) and fig1-oak-steeper-advance stand only under P1, which treats 48 tree-years as independent although there are 8 temperature values.
