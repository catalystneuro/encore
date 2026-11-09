I've written the claims file at `claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml`. The quote checker passes with 0 problems: 39 claims, 38 quotes and 38 statistical values. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10828195), with the Results, Discussion, Methods, the legends of Figs. 1–7, and the full supplement (Supplemental Figs. S1–S7, Tables S1–S6, Methods S1–S4). No PDF was supplied, so I saw no figures. The paper links no code, so I read none.

**Claims:**
- **39 claims:** 38 have quotes. The one without is the Table S5 climate values, which no sentence states, so it has an `inferred` note.
- **Statistics:** 17 claims carry statistics, 38 entries in all. They are regression significance, the Fig. 1 P = 0.004, the mixed-model F tests from Tables S1, S2, S3 and S6, and Tukey thresholds.
- **Criteria and expected values:** all 39 claims have a criterion; 13 also have expected values.
- **Shared methods in the opening comment:** four procedures, each cited, which the criteria refer to: the phenology regression, the treatment test, the interaction test, and the biodiversity effects.

**Details the paper leaves open, with the readings named:**
- **Phenology regressions:** fitted on each tree and year against its chamber's mean, or on the eight treatment-year means as Fig. 1 plots them. Air sensor at 50 cm or at 2 m.
- **Treatment model:** fitted on 2019–2021, as the Methods and Table S1 say, or on the reported years 2020–2021. For negative increments under the square root: untransformed, or shifted so the minimum is zero.
- **Mixture against monoculture contrasts:** within each year, or pooled over both years.
- **Net biodiversity, complementarity and selection effects:**
  - Each mixture tree is compared either with the treatment's mean monoculture value or with the monoculture tree in its own chamber.
  - Leaf traits enter as yearly tree means or as per-campaign values.
  - The test is a t-test against zero (Methods), with Tukey's HSD (legends) as a variant.
- **Growing degree days (GDD):** the excess over 5 °C, or the daily means above 5 °C. Chilling days end at bud swelling (Methods) or at leaf flushing (Fig. 2 legend). The negative exponential has two parameters, or three with an asymptote.
- **"Least-squares analysis" (P = 0.004):** a species-by-temperature interaction on bud swelling, or on growing season length.
- **Which year:** not stated for the beech Asat selection effect, the beech sugar effect under low moisture, or the beech diameter effect under low moisture.
- **Which value "reached":** the ΨPD of −1.9 and −1.2 MPa could be the lowest yearly or campaign mean, under low moisture alone or also combined with warming.
- **Units:** the mixture diameter differences are printed in cm, but Table S4 gives diameters in mm. Both units are named.
- **Table S6:** species and years pooled, or per species.
- **Table S4:** the test is not named; a one-way ANOVA or the mixed model are named.
- **Treatment magnitudes:** the averaging period.

**Missing from the paper:**
- **Figure values:** the R² and P values inside Figs. 1, 2 and S1 could not be read without the PDF.
- **Equations 3–4 (complementarity and selection effects):** garbled in the extracted text. I recorded a Loreau and Hector reading.
- **AGWB coefficients:** not printed. They are outside data from Annighöfer et al. 2016, named in the header.
- **Two internal contradictions:** the Results call the complementarity effect behind oak AGWB under warming and beech sugar under low moisture negative, while the Discussion calls it positive. The criteria report the sign found.
