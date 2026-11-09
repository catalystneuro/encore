I wrote the claims file at `claims/crcns-hc-14/10.1038-nn.4637.yaml`. It has 38 claims and every claim has a quote; none needed `inferred`. The quote checker validates the schema and finds every quote word for word. It flags 5 p-values it cannot find because they are printed as powers of ten (9.70 × 10−9, 3.9469x10-07, 8.85x10-05, 7.75x10-05, 6.45x10-05). I checked each of these against the text by reading it.

**Text read.** The version of record, which includes the main text, figure legends, Online Methods and the reporting summary, plus the supplement (Supplementary Figures 1 to 11 and Supplementary Tables 1 and 2). Nothing the results rest on is missing. Supplementary Table 1 is only an image and no PDF renderer was available here, so I took the cell totals per structure from the Results. I read the data descriptor only to know what the dataset holds.

**Code read.** github.com/buzsakilab/papers, folder `GGirardeau-BLAHpcInteractions-Package`, commit cdcec89 (2017-07-28). Where the Methods leave a detail open and the code settles it, the criteria follow the code. That covers:
- the explained variance formula, epochs and inclusion rules;
- the reactivation strength computation and its ±250 ms window;
- the two-sided Poisson threshold for ripple modulation;
- the danger zone speed;
- the 20-min windows, counted in cumulative NREM time;
- the sign of the pair contribution.

**Counts.** 68 statistical values across the statistics entries. 33 claims have a criterion; the other 5 are judged on their expected values alone. 12 claims have expected values. 10 are claims of absence, each judged on the paper's test.

**Details the paper leaves open, with the readings named:**
- **Which labels count as "BLA":** the BLA label alone, or the group BLA, BLV, LaDL, BMA and BMP. The 2,038-unit count should tell which one the paper used.
- **Ripple-modulation threshold:** the code's two-sided p < 0.001 is followed; 0.001 in each direction is a variant.
- **Sleep states:** these were scored by hand. If the dataset lacks them, the author has to state the substitute.
- **Laps counted in the habituation index:** all laps (Methods), air puff laps (legend) or left-to-right laps (code). The paper gives no test, so the readings are a Spearman correlation with training day per rat and pooled.
- **Post hoc correction in Fig 5a:** Bonferroni in the Methods, Tukey-Kramer in the legend and code. Both are run.
- **Gain smoothing in Fig 5b:** a 20-ms Gaussian (Methods) or the code's smoothing.
- **Piriform sessions in Fig 3d:** 14 in the Results, 17 in the legend.
- **Rate used for the Supplementary Fig 9 octiles:** run rate or whole-session rate. That claim, the skewed-rate claim (Fig 2c) and the air-puff-location claim have no test in the paper, so their tests are either taken from the code or named as readings.
- **Fig 6b measure:** the window mean is followed (code); the peak bin is a variant.
- **Ripple-rate test:** two-sided as the Methods' default; the code's one-sided version is a variant.

**Needed by a claim but missing from the paper and its code:**
- The script for the test-run correlations in Fig 7. Bins and intervals are open; the readings are 50-ms bins over the whole test epoch or over its laps only.
- The test of BLA firing rates on safe against air puff runs. The readings are rates over whole laps (the reading the absence claim is judged on) or within ±40 cm of the air puff.
- The shank-to-structure lists (`structures.mat`) and `poissonTest.m`, which are not in the package.
