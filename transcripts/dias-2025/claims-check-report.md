The claims file for DRYAD:bvq83bkk9 is ready for an attempt. I made eight corrections, and three questions remain open.

**Checker result** (after my edits): `claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml: 32 claims, 32 quotes, 58 statistical values, 0 problems`. It also showed 0 problems before my edits.

The header says the claims were written from the paper's code, so I downloaded that code from Zenodo to a temp folder. Its hash matches the one the header records. Most of the method matches: the age classes, predictors, year coding, Stan model, priors, sampler settings and seeds. So do the preliminary-model terms and which table rows they map to, and the lambda, VIF and Table S8 calculations. All 32 statistics and tolerances match Tables 1 to 3 and S4 to S8.

**Changes, by claim**
- **Header, main-model method:** the code drops a species-year when any column it pulls from the climate file is missing, not only the model's own predictors. It does this with fixed row numbers. I corrected the text and listed those row numbers.
- **table1-hy-year-slope:** `expected` was written as a mapping; it is now a list like every other claim's.
- **table-s1-species-consistency-hy:** the statement said all HY intercept effects agree within each species, but the claim only tests breeding temperature and year. I narrowed the statement to those two.
- **s4-s6-climate-variable-selection:** one example of an interval bound printed as 0.00 was wrong (its bound is 0.01). I replaced the examples with the bounds the tables actually print as 0.00 or -0.00.
- **s4-s5-climate-size-interactions:** the quote covered only the HY result and ended on an unrelated sentence. It now quotes the S4, S5 and S6 captions for all three findings.
- **s8-climate-trends:** the criterion didn't say how to read the 95% interval. The code prints it two ways, so both readings from the header now apply.
- **climate-trends-cannot-explain-wing-increase:**
  - I added autumn migration temperature to the statement, since the quoted sentence names it and the criterion tests it.
  - I dropped the phrase saying these effects "persist across age classes". The breeding temperature effect is not significant in spring AHY birds (Table 2).
- **s9-s11-expanded-ranges:** the criterion said these models reuse the main models' seeds. In the code the two HY models use seed 10, not 9. I corrected this and noted that this part of the code runs on the data preparation from the main script.

**Still open** (recorded under `checks`)
- **climate-explains-little:** the paper gives no way to measure how much variation climate explains. The two readings in the criterion come from the first reader, not the paper. I left them as written; if they disagree, the claim is blocked as underspecified.
- **s8-climate-trends:** the input table for Table S8 (`envdata3`) is not created anywhere in the code. The criterion counts a match under either of its two readings.
- **Outlier filter:** the Methods describe one but the code doesn't apply it. The author has to find out whether the deposited data are already filtered, using the readings the header lists.

Only the claims file was changed. Nothing is committed or pushed.
