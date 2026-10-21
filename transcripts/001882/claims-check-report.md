I checked the claims file for DANDI:001882 against the full text and made seven changes. The file is ready for an attempt.

**Checker result** (after my edits): `claims/001882/10.3390-genes16010043.yaml: 26 claims, 24 quotes, 0 statistical values, 0 problems`. Before the edits it also passed, with 25 claims and 23 quotes. The paper reports no statistical tests, so having no `statistics` is correct.

**Changes, by claim**
- **table1-bcva**: the cut-off for "partially reproduced" was at least 10 of 14 eyes. The paper gives no such number, so it is now "some".
- **gnomad-frequencies**: the cut-off "at least four of the six" was also invented. It is now "some".
- **m75-vmd-phenotype**: the criterion left out the superior macular nevus, which the statement names. It now checks the nevus on the colour fundus photo and the infrared image, as the text says.
- **vmd-acuity-preserved**: the criterion assumed the threshold lay between 20/40 and 20/50 in the better eye. But M73 may count as reduced because of his worse eye (20/100). The criterion now names both eyes and thresholds up to 20/100 as readings. These must all give the same result, or the claim is blocked as `methods_underspecified`.
- **table2-pathogenicity**: the FATHMM and MutationTaster columns had been left untested because the flattened table was said to be ambiguous. It is not: every row has seven entries, with "-" where a score is missing. I added the 12 values under expected with the default 10% tolerance. I also named PolyPhen-2's HumDiv and HumVar models as readings. The criterion now says the paper gives no rule for its Prediction column, and quotes what section 3.3 says the calls rest on.
- **table3-destabilizing**: the criterion tested all 25 values from Table 3 but listed only 3 under expected. All 25 are now listed, with 10% tolerance.
- **variant-domains** (new claim): where each variant sits in the protein (Figure 1, Results 3.1, 3.2 and 3.5) is one of the paper's main findings and had no claim. The paper names no source for its domain boundaries, so the readings are UniProt and InterPro. "Near" is undefined and is marked as open.

All other claims match the paper. None draws on anything but this paper.

**Still open**
- I could not confirm the Discussion paragraph numbers given in the sources. The flattened text marks no paragraph breaks, and there is no PDF.
- The paper does not say which MutationTaster output its "score" is, or which FATHMM model gave its coding scores.
- In Table 4, p.Asp423Glu adds 32 Da and 7 atoms, but one Asp to Glu change adds 14 Da and 3 atoms. The claim already notes this.

The `checks` entry is added with `ready: true`. Nothing was committed or pushed.
