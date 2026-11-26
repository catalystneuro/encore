I'm stopping without writing a claims file, because the SI Appendix is missing from `paper/`.

**What I read:** `paper/10.1073-pnas.2207052119.txt`, taken from Europe PMC (PMC9522358, open-access JATS). It is the version of record and holds the main text, figure legends and Methods. There is no PDF and no supplement under `paper/`. The text only gives the link to it: https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.2207052119/-/DCSupplemental

**Why the results need the supplement:**
- **Statistics:** Every model behind the reported P values is in SI Tables S1 to S10. The Methods (Statistical Analyses) leave the model details to the supplement: "For a detailed description of statistical analyses of all models, see SI Appendix, SI Statistical Analyses". Without it, I can't take fixed effects, interactions, outlier handling or random-effect structure from the paper. A claim would have needed these for:
  - CTmax by age and by oxygen level
  - medulla peak frequency over time and time²
  - heart rate by temperature range
  - depolarization onset, amplitude and recovery
  - the binary light responses
- **Findings shown only in the supplement:**
  - Table S1: no difference in swimming speed.
  - Fig. S1 and Tables S2 and S3: spiral swimming, loss of equilibrium and loss of response compared with controls.
  - Fig. S2A: the medulla decrease at 39 to 41 °C.
  - Fig. S2B: medulla activity in experiment 4.
  - Fig. S3A to C: depolarization amplitude and recovery time by oxygen level.
  - Fig. S3D: the drop before depolarization in every oxygen group.
  - Fig. S4: tectal response amplitude and how responses were classified.
- **Methods details:** The thresholds for medulla peak detection and the exclusion criteria are not in the main Methods. The supplement may give them.

**Code:** The paper's R code for the statistics and figures is deposited in the dataset itself (FIGSHARE:19640805). I did not open it, because my instructions forbid looking at the dataset's files. Whoever supplies the SI should also decide whether a reader may read that code as "the code the paper links".

**Result:** 0 claims, so 0 quotes, 0 statistics and 0 criteria. I created no files and ran no quote check. Once the SI Appendix PDF (with SI Statistical Analyses and Tables S1 to S10) is added under `paper/`, the reader run can be repeated.
