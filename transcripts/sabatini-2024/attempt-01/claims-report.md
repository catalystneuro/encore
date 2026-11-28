I wrote `claims/sabatini-2024.yaml`, and the quote checker passes it: 34 claims, 34 quotes, 21 statistical values, 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (Nat. Commun. 15:7007), full text from PMC11325044, including the Methods, figure legends and the data and code availability statements.
- **Supplement:** the extracted text of 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 and the basis-function derivation). I didn't need to open the PDF itself.
- **Code:** github.com/kaufmanlab/LDR-public at commit b65f28d.

**Counts**
- 34 claims, all with quotes and none `inferred`.
- 17 have `statistics`, 4 have `expected`, and all 34 have a `criterion`.
- Most numbers are ranges over the four datasets (M1-J, PMd-J, M1-N, PMd-N). One rule in the opening comment covers them: each dataset's value must fall inside the range widened by 10% of each bound.

**Details the paper leaves open, and the readings named**
- **Which 72 of the 108 conditions:** the code drops every third condition of a file order that isn't public. Readings: (a) condition number a multiple of 3; (b) distractor repeats identified from the maze geometry.
- **Trial selection:** (a) all successful trials; (b) delay above 400 ms. Both are compared against the paper's 1469 and 2014 trials.
- **Kinematic basis functions:** the function that builds them (`kinFuncEval`) isn't in the repo. Readings: (a) the raw velocity singular vectors integrated to position; (b) their skew-normal fits.
- **jPCA R2:** R2_Mskew_2D or R2_Mbest_2D. The pairing for the straight-against-curved test is also open.
- **Comparison windows for variance explained:** -150 to +850 ms, or the code's full -350 to +850 ms.
- **Eigenvalue noise null:** Poisson resampling (the Methods' main control) or trial half-splits (their second control, and what the code does).
- **Alignment noise repeats:** 36 (Methods) or 200 (code).
- **Tests named differently in the Results, Methods and code** (rank-sum against signed-rank): the Results' or Methods' test decides and the code's is a variant. The pairing for Fig. 5a is open.
- **Fig. 6b:** the Methods say 6 folds and lambda 0.1; the code uses 2 folds, lambda 0.01 and an SVD-reduced predictor. The code's version is a variant.
- **Fig. 6e location-from-kinematics regression:** there's no code for it. The kernel is either the Ornstein-Uhlenbeck kernel with length scale 10^3 or the Gaussian kernel with length scale 400.
- **Fig. 6c (location follows reach direction):** the paper states this only qualitatively. I named a circular correlation as the reading.
- **Decoder:** the Methods say "6-fold" but describe halves; the Results and code use 2 folds. The ridge penalty appears only in the code (10). GPFA latent count and bin size are given nowhere; I named 8 or 15 latents with 20 ms bins.
- **Rotation dimensionality:** what goes into the PCA is open (the loading columns, or the rotation's activity).
- **Supp. Fig. 8 absence claim:** the paper reports p = 0.04 to 0.96 and calls none of it a substantial drop, so it sets no threshold. The claim holds when every p is at least 0.036.

**Missing from the paper and its code**
- **Preprocessed data:** the code loads `.mat` files that aren't public; the paper says "code-compatible data" are available on request.
- **Code pieces:** `kinFuncEval`, GPFA, the location regression and the Poisson eigenvalue null aren't in the repo.
- **EMG:** Supp. Fig. 8 needs EMG to find the muscle-related dimensions, and I don't know whether the dandiset holds it. If it doesn't, only the hand dimensions are removed and the claim's outcome rests on that.
- **Output-potent dimensions:** the Methods don't say how they are found; only the code (`removePotent.m`) does.
