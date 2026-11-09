I wrote `claims/000785/10.64898-2025.12.12.694045.yaml`. The quote checker passes every quote but exits non-zero on two p-values it can't find. I read both in the text: the paper prints them with trailing zeros ("3.90 × 10⁻ 4" in fig2e-reliability and "2.50 × 10 -6" in fig5f-stability), which the checker doesn't recognise. The recorded values are correct, and I changed neither the values nor the checker.

**Text read.** The bioRxiv preprint, version 1, flattened from its JATS XML. It has the main text, the Methods and the legends of supplementary figures S1 to S13; there is no PDF. The paper's linked code is gitlab.com/fleischmann-lab/calcium-imaging/projection-difference at commit f478b34. It only loads and preprocesses the NWB files, plus one demo SVM notebook. The figure analyses are "to be released upon publication". The code settles four things:
- **Normalization:** "percdFF" (1 s median filter, running 10th percentile over 30 s, then divided by the SD).
- **Trial removal:** the NWB `is_bad_trial` column.
- **Tracked-cell labels:** red in at least 3 of 4 sessions (`min_3_sessions`).
- **Classifier:** `SVC(kernel='linear')`, with `LinearSVC` shown as a variant.

**Claims.** There are 36 claims, all with quotes. 19 have statistics (75 entries), 35 have criteria and 7 have expected values. They cover the neuron counts, the labeling check, the transformer and MLP classifiers, the Figure 2 response properties and identity decoding, concentration tuning and decoding, behavior and licking, identity and valence decoding in the Go/NoGo task, and the tracked-neuron slopes, CV, transferability and stability. The last claim, that the differences grow with learning, comes from the Discussion.

**Details the paper leaves open, with the readings named:**
- **Active-response sliding window:** anchored at the start of each frame, or centred on it.
- **Sparseness and mutual information formulas:** lost in the flattening. The reading is Vinje and Gallant sparseness and empirical mutual information.
- **Go/NoGo window aggregate:** mean or maximum. The folds are taken as 5-fold stratified, as for the passive datasets.
- **Figure 2H window:** 0–5 s (legend) or 1–5 s (Methods).
- **Sliding-window width:** 250 ms (legends) or 500 ms (Methods), in Figures 2J and 3D/E.
- **Reliability analysis:** the baseline window (the 4 s or the 5 s before odor onset), per-trial or pooled baseline statistics, and "more than half" counted over all odor trials or per odor.
- **Latency and proportion responding:** the sample is per trial or per neuron.
- **Count reporting:** per session over days 1–3 or days 0–3 (Go/NoGo counts); first session or session mean per mouse (Figure S2B).
- **Classes for the classifiers:** two classes, or three including untagged neurons.
- **Figure 4I/J valence scheme:** read as unconstrained valence on correct trials.
- **CV of tracked neurons:** combinations of valence × phase or odor × phase, and SD over the absolute mean or the signed mean.
- **Transfer and stability tests:** the Mann-Whitney samples are matrix entries or per-mouse means; the block pairs are all pairs or pairs sharing the training day.
- **Undefined windows:** "earlier", "later", "anticipatory" and the Figure 3C window width.
- **Claims with no test given:** judged on direction only, and the file says so.
- **The paper's own tests:** several are unnamed. Two-sided Mann-Whitney U with Bonferroni correction is presumed and labelled as presumed.

**Missing from the paper:**
- **Tables 2 to 8** survive as titles only. Without Table 5 (transformer hyperparameters), Table 6 (held-out animal pairs) and Tables 7 and 8 (MLP search space and settings), the transformer and MLP claims are blocked as `methods_underspecified` until those tables are supplied. That covers the F1 scores, attention timing and latent separation. Tables 2 to 4 (odorants and concentrations) are not needed to test the claims.
- **The equations** for the measures above are lost in the flattening.
- **The mouse counts don't agree.** The Methods say 18 mice but list 9 OB-p and 8 mPFC-p (17), while Figure S2B has N = 9 OB-p and 10 mPFC-p.
- **The 30 Hz dataset** is marked "don't use for now" in the code's README.

Nothing was committed.
