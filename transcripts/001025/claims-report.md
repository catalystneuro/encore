I wrote `claims/001025/10.1016-j.bioelechem.2023.108437.yaml` with 14 claims. All 14 quotes pass `tools/claims_check.py` with 0 problems, and the file validates against the claims schema.

**Text read:** the accepted author manuscript in PubMed Central (PMC10247516). That includes the full Methods (2.1 to 2.4), Results, Discussion and figure legends. The paper has no supplement and links no code. No PDF was available, so I could not read figure labels. The dataset title ("The impact of voltage on CANCAN focusing … four-electrode arrays of varying sizes") matches Fig. 7.

**Claims:**
- **Coverage:** Fig. 4 (2 claims), Fig. 5A, Fig. 5B/C, Fig. 6A, Fig. 6B, Fig. 7A, Fig. 7B, Fig. 7C/D, the Discussion's statement on array size, Fig. 8A, Fig. 8B, Fig. 9A/B and Fig. 9C.
- **Quotes:** all 14 claims have one; none needed an `inferred` note.
- **Statistics:** 4 claims carry them: Fig. 4 (p < 0.001, test not named), Fig. 5B/C (p < 0.05), Fig. 8A (p < 0.01) and Fig. 6A's comparison inside its criterion. The only test the Methods name is a two-sided Student's t-test at p < 0.05, with significance otherwise read from error-bar gaps.
- **Expected values:** 9 claims have them, at the paper's s.e. for Fig. 4 and 10% otherwise. The Fig. 8 ranges are widened by 10% of each bound.
- **Criteria:** all 14 claims have one. Three are claims of absence, judged on the Methods' t-test: Fig. 7B, Fig. 7C/D, and equal center uptake in Fig. 8A.

**Details the paper leaves open, and the readings named:**
- **ROI count:** 92 or 224 ROIs could be the count over both diagonals or per diagonal. ROI width is not given, so the ROIs are taken as contiguous along the diagonal (a standard choice).
- **Diagonals:** both averaged, or only the e1 to e3 diagonal.
- **"Most peripheral ROI":** the mean of the end ROIs, or each half-diagonal normalized to its own end.
- **Center ROI:** the single ROI nearest the center, or the mean of the two either side of it.
- **Source of reported numbers:** raw dish means, or the LOESS fit. The LOESS span is not given, so the standard 0.75 is used and named as a standard choice.
- **Normalization (Fig. 8B):** ratio of means, or mean of per-dish ratios.
- **Fig. 4 test:** not named in the text. Readings: Student's t-test or Welch's t-test.
- **Peak width (Fig. 6B):** not defined. Readings: full width at half the height of the peak above the trough, or the distance between the troughs. The claim is blocked if the two disagree.
- **"Trough":** taken as the paper's own "least affected area", the lowest ROI between the center and the electrode.

**Missing or problematic in the paper:**
- **Fig. 7 voltages:** only 2.4 and 5.6 kV appear in the text. The other voltages are printed only in the figure, so the attempt has to take them from the dataset.
- **Array size:** the Discussion's claim that targeting does not depend on array size cannot be isolated. The small array got 4 packets and the large one 40, and Fig. 6B shows packet number alone changes targeting. That claim is judged on amplitude independence holding in both arrays, with the confound stated.
- **Fig. 8A typo:** the text says "~120 a.u. for packet 1", which contradicts the same sentence. I read it as Packet 2 and said so in the criterion.
