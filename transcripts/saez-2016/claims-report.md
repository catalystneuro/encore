I wrote `claims/saez-2016.yaml`, and the quote checker passes it: 16 claims, 16 quotes, 20 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (PMC4739708, open access), flattened from JATS XML: main text, Methods and the legends of Figures 1 to 3. The paper has no supplement and links no code. Its simulations were run in R, but the code is not given. No PDF was needed. I read the dataset's description only to see what the dataset holds.

**Claims:** all 16 have a quote, 10 have statistics and 16 have a criterion. They cover:
- the cell counts;
- control outcomes (1 LTP, 3 LTD and 24 no change out of 28), no net plasticity, and the mean changes by recording mode;
- voltage-clamp and current-clamp results being the same;
- no dependence on initial strength, in control and in bicuculline;
- the example cells in Figure 1D and Figures 2C and 2D;
- bicuculline outcomes (7 LTP, 9 LTD, 10 no change out of 26) and the mean change in each of those groups;
- bicuculline raising the share of cells that change, from 4/28 to 16/26;
- equal means but a larger variance in bicuculline;
- the Figure 3 Kolmogorov-Smirnov tests, the random-mixing simulation and the segregation parameter.

Three Figure 3 claims are `with_inputs`: they need the authors' earlier single-cell stimulation data (their reference 17), and the paper does not say where those data are.

**Details the paper leaves open, and the readings named:**
- **Post-pairing window:** all post-pairing sweeps; the first 10 minutes; or the last 10 minutes.
- **Per-cell t-test:** on individual sweeps, or on the 1-minute bin means.
- **How the peak is measured:** the paper says nothing. I fixed a standard choice (pre-stimulus baseline, peak up to 50 ms after the stimulus), with a 30 ms window as a variant.
- **Test of no net plasticity:** the paper's Student's t-test could be a one-sample test against 0 or a paired test. Its printed p > 0.8 does not fit its own mean and SD, which give p ≈ 0.08.
- **Correlation with initial strength:** the paper only says "correlation". I fixed Pearson, with Spearman as a variant.
- **Simulation:** sampling with or without replacement; one seeded run, or 1000 runs; and how the segregation parameter biases the sampling, read as P(same) = p + S(1 − p).
- **Example cells:** the paper does not say which cells are shown.
- **No test reported:** the paper gives no test for the difference in proportions, so Fisher's exact test is a variant I chose.
- **What ± means:** the arithmetic shows it is the SD across cells. Tolerances on means are the standard errors worked out from the paper's SD and n.

**Inconsistencies in the paper, recorded in the file:**
- The bicuculline cells are called current clamp in the Results but voltage clamp in the Methods and Figure 2, and number 26 in the Results against 27 in the Methods.
- The Results swap the control and bicuculline means (-3.5 against -3.8) and their figure references. I followed the legends.
- The control histogram is cited as Figure 1A in the text but is Figure 1C in its legend.
- The Figure 3A legend's colours are the reverse of the Results' wording.
- The single-cell dataset has n = 42 in the Methods and 43 in the Results.

**Missing:** the single-cell stimulation data and the simulation code, which the three Figure 3 claims need.
