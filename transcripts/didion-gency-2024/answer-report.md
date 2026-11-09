I answered all three questions and set `answered: 2026-10-27` on each. `claims_check.py` passes with 0 problems. Nothing was committed or pushed.

1. **fig4-beech-warming-none: the square root of negative starch, sugar and Asat values.** The paper doesn't say. It only has the table footnote "square root transformation has been used" and never mentions negative values or a constant. The criteria now apply readings S1 and S2 to these three traits as well as to the increments, and add a new reading, S3, which drops negative values (R's `sqrt` returns NaN for them). This covers all the treatment-test claims that use these traits, `tables6-no-seasonal-variation` and the interaction test.

2. **tables2-phenology-no-interaction: which years enter the interaction model.** The text doesn't say, but the F and p values printed in Tables S2 and S3 show how many years each model used:
   - Bud swelling and development duration have 1 df for year, so two years (2020 and 2021). Example: oak Y x I "9.37 (0.003)".
   - Onset of senescence, senescence duration, growing season length and all Table S3 traits have 2 df, so three years (2019 to 2021).
   
   The criteria now use this split (reading Y1) and report 2020 and 2021 for all traits (Y2) as a variant. The same arithmetic shows Table S1 also used three years ("5.22 (0.006)"), which supports reading T1 for the treatment test; I noted this in the file.

3. **tables6-no-seasonal-variation: which years and which F tests.** The paper doesn't say. It gives only the model formula, calls the tests "ANOVA tests", links no code, and Table S6 has no year or species column. The criterion now names as readings:
   - **Years:** y1 is 2019 to 2021, the years of the treatment test that Table S6 is cited for; y2 is 2020 and 2021.
   - **F tests:** F1 sequential (nlme's default) and F2 marginal.
   
   The outcome is still the one all readings give. The attempt found that marginal tests match Table S1 on the data, but that can't be confirmed from the paper, so I couldn't use it to settle the question.

No claim statement or expected value changed.
