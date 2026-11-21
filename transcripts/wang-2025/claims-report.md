I've written `claims/wang-2025.yaml` with 29 claims. The quote checker passes except for one value. The striatum p-value in the Extended Data Fig. 6 legend is printed as "p = 3e7". A p-value can't be above 1, so I recorded it as 3e-07, and the criterion says so.

**Text read**
- The version of record (Nature Neuroscience, 18 Nov 2025): main text, figure legends, Methods and the Extended Data legends.
- The Supplementary Information PDF, read from its extracted text: the session-independent autoencoder section, Supplementary Table 1 and Supplementary Figs. 1–2.
- Nothing the results rest on is missing. I did not read the Reporting Summary or the Supplementary Videos.

**Code read**
- `druckmann-lab/MapVideoAnalysis` at commit 7d276243. It settles most details, including the region groupings, filters, epoch windows, Bonferroni factors, ridge penalties, the 64-trial split and how the improvement percentages are computed.
- The deep-network repository `kurgyis/BehaviorVideo` could not be fetched: the clone asked for login, so it is private or gone.
- The code that decodes choice from video (all of Fig. 6, and the single-trial labels Fig. 7 uses) is in neither repository. MapVideoAnalysis only reads its precomputed output.
- Some of the code's printed outputs don't match the paper. The method improvements print as 174/377/83% against the paper's 155/330/76%. The claims keep the paper's numbers.

**Counts**
- 29 claims; 29 have quotes, so none needed an `inferred` note.
- 21 have statistics; all 29 have criteria; 19 have expected values.
- Everything is `data: dataset`, since the paper says all its data are on DANDI. Whether the dandiset holds the raw video is for the author to find. If it doesn't, the authors' outside deposits are named as the alternative input: processed data on Zenodo (10.5281/zenodo.16740783) and an unpinned Google Drive folder of embeddings.

**Details left open, and the readings named for each**
- **Fig. 5 time offsets:**
  - A neuron's best offset is either the arg max of the fold-averaged curve (the Methods' wording) or the mean of each fold's best offset (the code; its printed means match the paper's).
  - The Bonferroni factor is ×3 or ×4.
  - The code runs the test two-sided; that is named as a variant of the paper's one-sided test.
  - The FDR threshold is Q = 0.05 (Methods), with the code's 0.01 as a variant.
- **Fig. 6 decoder:** either L2 logistic regression on the 5-frame embedding window, or on a single frame. The pre-sample window is either all bins before sample onset (−3 to −1.85 s) or the last 0.5 s. The test behind "increased significantly" isn't named.
- **Fig. 6d clustering:** the session filter in the Methods either applies only to Fig. 6e or to both 6d and 6e.
- **Marker vs embedding decoding (0.88 vs 0.96):**
  - Window: the whole response epoch or its second half.
  - Marker features: the better of jaw or nose, jaw alone, or all three markers.
  - Test: Wilcoxon signed-rank or paired t-test.
- **Correlation with performance (r = 0.33):** the AUC from the delay epoch or from the sample plus delay epochs; Pearson or Spearman.
- **Fig. 7b jaw height:** the test isn't named; Mann–Whitney or Welch t-test. The vL/vR cut is taken as the predicted class.
- **Fig. 7 classifier:** logistic regression with leave-one-out penalty selection (Methods), with the code's RidgeClassifierCV as a variant. The uniformity test uses 10,000 shuffles (Methods), with the code's 1,000 as a variant.
- **Extended Data Fig. 1 (196 neurons):** whether it uses the single split or the cross-validated values.
- **Supplementary Fig. 2:** the noise level "100 µm variance" is read as either a standard deviation of 100 µm or a variance of 100 µm².
- **Session-independent autoencoder:** what a "recording" is (one probe insertion, or one area of a session); whether the difference is relative or absolute; which sessions are trained on; and the test.
- **Network training settings** for the end-to-end network and the autoencoder are in neither the paper nor the code read; the author will state the ones used.
- **Fig. 2 method comparison:** the code's neuron filter (0.005) is named against the Methods' 0.01.
- **Extended Data Fig. 10:** the paper gives no measure of "largely consistent", so I set one from panel c.
- **Fig. 2 ordering across methods:** whether it means the strict order of all five areas or only medulla first and thalamus last.

**Missing from the paper**
- The video choice decoder: its method and code (affects all Fig. 6 claims and the Fig. 7 trial groups).
- The training settings for the deep networks.
- The main text prints the medulla s.e.m. as 0.06; Extended Data Fig. 3 shows it should be 0.006.
- Animal counts disagree: 28 mice in the Methods, 22 in the Supplement.
- The tracked markers disagree: jaw, nose and tongue in the Results, jaw, paws and tongue in the Methods.
