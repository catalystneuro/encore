I wrote `claims/komori-2026.yaml`. The quote checker passes: 23 claims, 21 quotes, 28 statistical values, 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint (doi:10.64898/2026.05.27.726399, posted June 1, 2026), with its Methods, all figure legends and the legends of Supplementary Figures 1 to 12. I read Supplementary Figures 3 to 6 from the images supplied with the text. The linked code is github.com/moritalabC201/WF_deep-learning at commit 405a720. It holds template notebooks for the stimulus experiments only. Nothing in it loads DANDI:001425 or builds the resting-state labels.

**Claims.**
- **Totals:** 23 claims. 21 have quotes; 2 are marked `inferred` because they are read from Supplementary Figures 5B-C and 5F-G. 21 claims carry statistics. 9 have criteria for the resting-state analysis; the other 14 criteria say "not testable".
- **Resting state, 6 claims, testable on DANDI:001425:**
  - decoding above the null models (validation AUC about 0.82 against 0.61);
  - validation loss and accuracy against the null models;
  - a 0.1 Hz feature filter is needed, and 2 Hz does not decode above chance (judged as a claim of absence with the paper's paired t-test);
  - 10 ICs and a 1.5 s window give the best AUC, though no comparison is significant;
  - the maximum VIF is 9.0 with 10 ICs;
  - SHAP for the medial anterior IC (IC7) rises before IC6 and IC4.
  
  Several expected values are read from the figure images, so their tolerance is 10% of the value read.
- **Stimulus experiments, 17 claims:** these cover the somatosensory, visual pattern and oddball experiments. The paper's own recordings are "available from the corresponding author upon reasonable request" and deposited nowhere. They stay `data: dataset` and are not testable on DANDI:001425.

**Details the paper leaves open, with the readings named (R1 to R10 in the opening comment):**
- **R1, which mice and sessions:** all 25 mice, or the three mice the Cross-validation section names. It also does not say which 2 or 3 resting sessions per mouse.
- **R2, preprocessing:** the paper's own hemodynamic correction on the raw frames, or the dataset's corrected signals as a variant.
- **R3, pupil measure:** the deposited ellipse diameter, or the distance between the left and right pupil keypoints.
- **R4, samples per epoch:** only the window from 3 s before to 0.5 s after the peak, or the whole epoch with labels set inside that window.
- **R5, epoch selection:** none, or the code's pre-peak exclusion rule.
- **R6, choice of ICs:** the paper picks them "by visual inspection", which cannot be repeated. A stated rule replaces it.
- **R7, fold unit:** the 40 s epoch or the whole recording.
- **R8, null shuffle:** training labels only, as the code does, or training and validation labels.
- **R10, Deep SHAP:** the Methods (first positive sample, mean model output as background) disagree with the code (every 20th validation sample as background). The Methods come first and the code is a variant.
- **SHAP "increase" onset:** the paper does not define it. The readings are the first window significantly above null, or the time of the peak.

**What the paper is missing or contradicts:**
- The stimulus-experiment data are not public, so none of those findings can be tested.
- Session counts differ between text and legends: 143 against 109 selected visual-pattern sessions (740 against 741 in all), and 79 against 105 oddball sessions.
- The Results say the grating rotates clockwise; the Methods say counterclockwise.
- Some numbers in parentheses after the SHAP results (0.013, 0.00020 and so on) are not labelled as p-values or SHAP values, so I did not record them as statistics.
- No code covers the resting-state analysis.
