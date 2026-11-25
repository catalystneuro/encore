I've stopped and written no claims for chan-2024. `claims/chan-2024.yaml` does not exist and nothing else in the repository changed. The paper's Methods and its supplement are missing from `paper/`, and the protocol (Reader, step 1) says to stop in that case.

**Text read:** the author manuscript of doi:10.1126/science.adi0858 (NIHMS2120560, PMC12704221), from `paper/10.1126-science.adi0858.txt`. It has 12 pages: the main text, references and the legends for Figs. 1 to 4. The PDF is 1.5 MB, so it is most likely the same manuscript, but I could not open it to confirm (no PDF reader is installed here).

**What is missing:**
- **Methods:** the main text says "Materials and methods are available as supplementary materials" (ref. 28). The manuscript itself says only "Refer to Web version on PubMed Central for supplementary material."
- **The supplement:** figs. S1 to S9 and tables S1 to S13. The findings depend on them directly:
  - the pollinator-exclusion fruit-set results (tables S3, S4);
  - the oxidation degradation rates (table S9);
  - the field visitation model (tables S10, S11);
  - the wind tunnel sample sizes and tests;
  - the 40% hawkmoth share of fruit set (table S3);
  - the compound reactivity comparison (table S12) and the model years (table S13).

  Without them, the measures, tests, sample sizes and the experiments' data structure can't be fixed for any criterion.

**Not done:** I did not read the linked code (Zenodo 10.5281/zenodo.8411927, riffelllab/Chan-et-al), and I did not run `claims_check.py` because there is no claims file.

**To proceed:** add the Science supplementary materials PDF (Materials and Methods, figs. S1 to S9, tables S1 to S13) to `paper/` and rerun the reader.

**Claims:** 0, so none with quotes, statistics or criteria, and no open details or readings recorded.
