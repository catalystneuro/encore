I checked the claims file for DANDI:001354 against the paper and made two changes. I recorded the check as ready.

**Checker result:** `claims/001354/10.1038-s41586-024-08282-3.yaml: 32 claims, 32 quotes, 5 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **ed12cd-expression-baseline:** The criterion defined each cell's "baseline" as the mean of the sweeps before DCZ, but the paper never defines a baseline. That was the writer's own choice. I now name it as open, with two readings: the mean of the pre-DCZ sweeps (B1) or the first included sweep (B2). I also named the sweep and cell exclusions taken from fig4i-rmp, which the criterion had left out. If the readings give different results, the claim is blocked as underspecified.
- **ed12g-expression-rmp:** The legend says RMP shifts were "not specifically linked" to expression. That can mean no correlation in either group (S1), or no correlation specific to the DCZ plus mCherry group (S2). Both readings are now named. The paper's table of these correlations (Extended Data Fig. 12h) cannot be read from the text. I also added the missing sweep exclusions and their readings.

All other statements, sources, quotes, statistics (Z and P for Fig. 4i, Fig. 4j and Extended Data Fig. 12b; the tests for Extended Data Figs. 3a and 5c) and tolerances match the paper. None of the statistics is a threshold used to count units. The claims cover the main findings across Figs. 1 to 5 and the Extended Data, and all of them come from this paper.

**Still open (recorded in `checks`)**
- **Extended Data Fig. 12h:** The paper's correlation values (r and P per group) can't be read because no PDF of the main article was supplied. So ed12cd, ed12ef and ed12g have no expected values from the paper.
- **Slice method details:** The Methods leave several details unfixed, and no code is published (the paper says scripts are "available upon request"). These are the change windows (W1, W2), the unit of the mixed model (M1, M2), how action potentials are detected (A1, A2) and the window for input resistance. The readings already named in fig4i-rmp stand. One random intercept per mouse is my reading of the Methods' statement that the model accounts for several cells per animal.
- **Exclusion threshold unit:** The paper prints the 500 input-resistance cutoff as "mΩ" (milliohms). Reading it as megaohms is based on context only.

**Ready:** yes. Nothing was committed or pushed.
