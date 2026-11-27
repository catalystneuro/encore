I wrote `claims/longcore-2024.yaml`. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC11418196, open access JATS), with main text, Methods, Results, figure legends and Discussion. The paper cites no supplement and no PDF was available. The paper links no code; the analyses were run in JMP Pro 17 and Prism.

**Missing from the paper text:** Table 1 is gone. Only its title came through, so the 12 per-condition mean suppressions are not in the text. The abstract gives four of them, but I did not use those. As a result, the claims that rest on Table 1 have direction criteria but no expected values: `table1-suppression-0p5-and-above`, `table1-increase-0p01`, `lower-cct-less-suppression` and `cct-effect-grows-with-intensity`. Someone with the table should add the values.

**Claims:** 13, all with quotes.
- 6 have statistics: the Tukey-Kramer test, the GLM overall and per-term p-values, the sex term, four 95% CIs for the sex predictions, two CIs for individual mice, and the cFos t-test.
- 13 have criteria.
- 4 have expected values: the AICc values and their differences, the sex predictions, the individual extremes, and the cFos means.

**Quote check:** one item remains. The female CI is printed as "2.1% increase to 8.9% decrease", and I recorded it as a suppression of -2.1 to 8.9. The checker can't find "-2.1" in the text; I confirmed it by reading.

**Details the paper leaves open, and the readings named:**
- **Percent change:** how a mouse with no activity in the prior-day ZT14–15 window is handled. I left such values out as a standard choice, with the count reported.
- **Illuminance in the GLM:** entered in lux or in log10 lux.
- **GLM effect tests:** likelihood-ratio (JMP's default) or Wald.
- **Log link:** a normal response with a log link needs positive fitted means, but some suppressions are negative. The fit is run as JMP does, and any failure to converge is reported.
- **Tukey sentence ("only significantly greater for 50 lx at 1750 K"):** (a) illuminances compared within each CCT; (b) CCTs compared within each illuminance.
- **Effect size for categorical CCT:** (a) the largest effect-coded parameter; (b) CCT refit as continuous in kelvin. "Several times" is read as a ratio of at least 2.
- **Sex and mouse-ID models:** main effects only, with no interactions.
- **Sex predictions:** model predictions are the main reading; raw means by sex are a variant.
- **Individual effects in percentage points under a log link:** (a) the effect-coded mouse parameters; (b) each mouse's mean predicted suppression minus the overall mean.
- **cFos:** how the three observers' counts are combined. The mean over observers is the main reading; each observer alone is a variant.

**Inconsistency in the paper:** the reported cFos means and s.d. (n=6 per group) give t ≈ 1.28, not the reported t(10)=0.9409. That claim is therefore judged only as an absence at p > 0.05, and the paper's t and p are not expected values.
