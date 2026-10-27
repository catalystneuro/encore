I've taken up the three answers and re-run every claim they affect. Three outcomes changed and the rest stayed the same. `tools/entry.py lock` and `all` pass with 0 errors (the notebook runs in 78 s in a clean environment), the handover is in `executed/dryad-4j0zpc8hz-didion-gency-2024/handover/`, and nothing is committed.

I changed the helper (`oaktrees.py`), the notebook (header, readings text, new loops, every affected conclusion, summary), the README and the attempt record. Each affected claim's notes now open by saying what the answer changed. Under S3, I compute the reported raw differences only on the rows the model keeps. That is my own choice, and it is recorded as a deviation.

**Q1. Square root of negative starch, sugar and Asat values** (fig4-beech-warming-none and the claims that share the question)

The answer: the paper does not say. Starch, sugar and Asat now take S1 and S2 like the increments, plus a new reading S3 (negative values dropped), which applies to the increments too. Each treatment-test claim now runs under twelve readings, up from eight.

| Claim | Before | Now |
|---|---|---|
| fig4-beech-warming-none | blocked, methods_underspecified | blocked, methods_underspecified: starch 2020 is significant under T1 on yearly means with S2 (p 0.041) and S3 (p 0.018), not with S1 (p 0.099) |
| fig4-oak-warming-growth-2021 | partially_reproduced | **blocked, methods_underspecified**: under T2 with S3 no 2021 contrast is significant (height p 0.054), so the readings now differ |
| disc-oak-warming-no-carbon-change | reproduced | reproduced (smallest p 0.30) |
| fig4-beech-mr | partially_reproduced | partially_reproduced (4 of 5 under S1 and S2, 3 under S3) |
| fig4-oak-mr | partially_reproduced | partially_reproduced (6 or 7 of 8) |
| fig4-beech-wmr | blocked | blocked (S1 and S3 give not reproduced, S2 gives partially reproduced) |
| fig4-oak-wmr | reproduced | reproduced (8 of 8 under every reading) |
| fig4-wmr-same-as-mr | blocked | blocked (2 of 216 contrasts significant, under S2 only) |
| disc-nsc-unchanged-drier-soil | reproduced | reproduced (smallest p 0.059) |

**Q2. Which years enter the interaction model** (tables2-phenology-no-interaction)

The answer: the criteria now use Y1, which is bud swelling and development duration on 2020 and 2021 and the other traits on 2019 to 2021. Y2 (2020 and 2021 for all traits) is reported as a variant. This replaces my earlier T1 and T2, and S3 also applies here.

| Claim | Before | Now |
|---|---|---|
| tables2-phenology-no-interaction | not_reproduced | not_reproduced (oak development duration under MR p 0.14 to 0.67; 6 or 2 other significant contrasts under Y1) |
| tables3-beech-warming-no-interaction | blocked | blocked (absence holds under 3 of 24 readings under Y1) |
| tables3-oak-warming-diameter | not_reproduced | not_reproduced |
| tables3-beech-mr-diameter | not_reproduced | not_reproduced |
| oak-mr-no-interaction | blocked | blocked (3 of 24 under Y1) |
| tables3-beech-wmr-height | not_reproduced | not_reproduced (p 0.23 to 0.61) |
| tables3-oak-wmr-diameter | not_reproduced | **reproduced** |

The new tables3-oak-wmr-diameter result rests on one reading. Under Y1 with S3, the 2021 difference is +1.38 (p 0.023), within 1.4 ± 0.14, and the criterion asks for only one reading. That difference comes from the tree-years S3 keeps, after 9 negative increments are dropped. Under S1 and S2 it is +1.69, which is outside tolerance, and the record notes say so.

**Q3. Years and F tests for Table S6** (tables6-no-seasonal-variation)

The answer: the paper does not say. The criterion now names years y1 and y2 and F tests F1 (sequential) and F2 (marginal) as readings, together with S1 to S3.

| Claim | Before | Now |
|---|---|---|
| tables6-no-seasonal-variation | not_reproduced | **blocked, methods_underspecified** |

With sequential tests, at least one trait has p ≤ 0.05 under all 24 readings; Asat is at p ≤ 0.043 under every one. With marginal tests, all three traits have p > 0.05 under 3 of the 24 (2020 and 2021, monocultures, both species pooled). The readings disagree, so the claim is blocked.

**Totals** are now 17 reproduced, 3 partially reproduced, 7 not reproduced and 12 blocked, up from 16, 4, 9 and 10.
