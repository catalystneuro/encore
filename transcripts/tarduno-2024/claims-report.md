The claims file is written at `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`. It has 17 claims (1 link check and 16 findings), and `tools/claims_check.py` passes it with 0 problems. Nothing was committed.

**Text read:** the version of record, from Europe PMC (PMC11271266, full-text XML). This includes the Methods, Data Records, Technical Validation, the legends of Figs. 1 to 3, and Tables 1 and 2. As a Data Descriptor, the paper has no supplement. It also has no code: it states no custom code was used and names PmagPy without a version, so no repository was read.

**Counts:**
- **Quotes:** all 17 claims have one. One quote is cut with "..." to leave out the word "rather".
- **Statistics:** none, because the paper reports no tests.
- **Expected values:** 7 claims have them. The main ones are Table 1 (M590 and the maximum field for each of the 12 crystals), the Table 2 MAD and R2 values for the 9 fitted glass specimens, the 12% success rate with the 13/12 split by AF pre-treatment, the 0.2 to 0.5 μT baseline, and the 14053g1 example.
- **Criteria:** 15 claims have one.

**Details the paper leaves open, with the readings named:**
- **MAD:** (a) a free line fit, (b) a line anchored to the origin, (c) a free fit to the three-point smoothed vectors.
- **pTRM check %:** normalized by (a) the original pTRM at that temperature or (b) the length of the fitted TRM segment. The check's own pTRM subtracts either (i) the field-off vector measured just before it or (ii) the field-off vector at the same temperature.
- **M590 in Table 1:** (a) the vector difference 590.1 minus 590.0 or (b) the magnitude of 590.1. Either one uses (i) the first replicate or (ii) the mean of the replicates.
- **Consistent or inconsistent replicate directions (Fig. 3):** (a) Fisher k compared between steps, (b) Watson's randomness test at p < 0.05.
- **Regular TRM acquisition, a changing field (Fig. 2), AF cleaning causing "no significant change", and stability at 400 °C:** each has two readings, built from the paper's own 15% pTRM tolerance or the specimen's MAD.
- **Directions "not random":** the paper names no test, so Watson's test is used as a standard choice.
- **Selection thresholds:** Table 2 lists ss6 as failing R2 at 0.91 while ss43 at 0.90 does not fail, and no MAD threshold is given. The claim therefore reports each listed failure against the stated thresholds without judging it.

**Missing or inconsistent in the paper:**
- **Figures not seen:** no PDF was supplied. The nominal paleointensities printed in Fig. 1 and the temperature ranges the arrows mark in Figs. 1 and 2 are therefore not recorded; the criteria use the Table 2 ranges instead.
- **Table footnotes:** the text lacks the footnote legends of both tables. My reading that the Table 2 marks separate specimens without and with AF pre-treatment is inferred and labelled as such.
- **14053g1 example:** the Technical Validation example for 14053g1 (8e-12 A m², 0.2 μT) conflicts with Table 1 (3.203E-09 emu, 0.51 μT). Its numbers match 12040g1, so both readings are named.
- **Rounding in Table 1:** its maximum-field values are 1 to 3% above what the formula gives from its own M590 column. That is within the 10% tolerance.
- **Sample name:** the Results cite "12041g1" where the Fig. 3 legend and Table 1 have 12040g1.
- **Interpretation:** the claim that the glass was magnetized by an impact plasma and that there was no long-lived dynamo rests on ref. 1 and on models. Its claim is included but marked as not tested; it is judged only from the outcomes of the related data claims.
