I wrote `claims/chan-2024.yaml` and did not commit it. The checker passes: 27 claims, 26 quotes, 26 statistical values, 0 problems.

**Text read**
- **Paper and supplement:** the author manuscript (PMC12704221) with the Supplementary Materials of the version of record: Methods, Equation S1, Figs. S1 to S9 and Tables S1 to S13. Nothing the claims need is missing. I opened PDF pages 9 to 12 only to read bar labels and the table inset in Fig. 2D.
- **Code:** github.com/riffelllab/Chan-et-al at commit ffc1559 (the release on Zenodo, 10.5281/zenodo.8411927). It has one R script that runs the pairwise proportion tests for Fig. 1E (R defaults, Holm correction) and one notebook that only plots Fig. 2D. There is no code for Fig. 3, Fig. 4 or Tables S9, S11 and S13. The repository also holds data files (Fig. 3B, Fig. S7, VOCUS traces, GC-MS, field sensors, GEOS-Chem output). I did not open them, and the opening comment lists them in case the Dryad deposit lacks those data.
- **Dryad record:** its description covers only the GEOS-Chem modelling.

**Claims**
- 27 claims in total. 26 have quotes; one (Table S6 emission rates) is marked inferred.
- 16 record the paper's statistics and 18 have expected values with tolerances.
- 26 have criteria. The one without is the reported values of visits per night, which its expected values settle.
- Six are claims of absence, each judged on the paper's own test: the Fig. 1E groups, the non-monoterpene compounds in Fig. 2D, the scent blend in Fig. S5, O3 and NO2 alone in Fig. 3B, the proxy mixture against the controls in Fig. 3B, and real against synthetic scent in Fig. 3D.

**Details the paper leaves open, and the readings named**
- **Fig. 1D:** the test behind Z = 17.67 is not named. Readings: a chi-square test on the Table S2 groups, or a two-proportion z-test on hawkmoths, all moths and butterflies, or all bees and wasps.
- **Table S9 / Fig. 2D:**
  - Which time windows count as the O3 and NO3 stages: the settled half of each stage, or the whole stage.
  - What the NO3 stage is compared with: clean air, or the O3 stage.
- **Wind tunnel (Fig. 3B, S7):**
  - The "50% decrease" can be relative or in percentage points.
  - The proportion test can be a z-test without continuity correction, or R `prop.test` with it.
  - The letters can come from uncorrected tests or Holm-corrected ones.
- **Field GLM (Fig. 3D):** counts rescaled to 49.5 h with no offset, or raw counts with log(hours) as an offset. The first reading gives exactly the coefficients and standard errors of Table S11 from the counts in Table S10.
- **Recognition distance (Fig. 4):**
  - The scent becomes unrecognizable when either compound reaches its threshold, or only when both do.
  - The NO3 map uses NO3 alone, or NO3 plus O3.
  - Concentrations are converted at the model cell's temperature and pressure, or at a fixed number density.
  - Wind speed is taken from the mean wind vector, or as a mean speed.
  - The preindustrial factor map is regridded by nearest cell or by bilinear interpolation.
  - A city is mapped to the cell containing it, or by interpolation.
  - "Most populated regions" is counted by cities, or by population.
- **Fig. S9:** population raw or log-transformed, and R² plain or adjusted.
- **Interannual comparison:** "orders of magnitude" read as a factor of 10, on log ratios or on |ratio − 1|.
- **Others:** the threshold for an active GC-EAD peak, which samples are averaged for Table S6, how the share of fruit set due to night pollinators is computed, and how the Table S1 means are taken.

**Inconsistencies in the paper, recorded for the author**
- Fig. 2D and Table S9 give different values for benzaldehyde and eucalyptol, and the Fig. 2D legend says "all differences P < 0.001" while Table S9 shows non-significant results for the non-monoterpenes.
- The GLM link is called "logistic" in the main text and Table S11, and "log" in the Methods.
- The 12.1.0 model run has 72 vertical levels in the Fig. 4 legend and 47 in the Methods.
- Fig. S9 reports F(2, 96), which implies 99 cities, while Table S13 lists 97 and the text says 98.
- The years of the field observations differ between the main text and the Methods.
- Table S12 itself shows O3 reacting faster than NO3 for α-terpinene and the green leaf volatiles, against the claim that only two sesquiterpenes are exceptions.
- Table S13 lists only 42 of 97 cities with a decrease of 75% or more, while the text says this holds in most populated regions.
- The EAG statistics in the Fig. S7 legend are garbled, so the criterion does not use them.

**Missing from the paper**
- The dose-dependence claim (more or less NO3 exposure gives more or less loss) has no data shown, so it can be tested only if runs at several doses exist.
- Only Fig. 3B prints bar values, and only the zero proportions for Hyles. No other wind-tunnel proportion is given in the text, so the other Fig. 3B claims rest on tests and on the 50% figure.
