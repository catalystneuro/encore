I wrote `claims/memar-2026.yaml`. The quote checker reports 20 claims, 20 quotes, 0 problems. Nothing was committed.

**Text read**
- arXiv preprint v1 (2606.11415v1, dated 11 June 2026), the full text under `paper/`: main text, Methods II A to H with Algorithms 1 to 4, Results, Discussion, and the appendix Tables II and III and Fig. 6.
- There is no supplement and the paper cites none, so nothing the results rest on is missing. I did not need the PDF.
- Code: github.com/neurovium/SpatiallyMaskedRegression at commit 244dcdb (2026-06-24). That commit is two weeks after the preprint, and the code describes itself as a "fixed" version of earlier code. It may not be the code that produced the reported numbers.

**Counts**
- 20 claims, all with quotes, none marked inferred.
- No statistics fields: the paper reports no tests or intervals, only mean ± SD.
- 11 claims have expected values. The tolerance is the paper's stated SD: across subjects for averages, across electrodes for per-subject values.
- All 20 claims have criteria.
- 10 claims use DANDI:000055 (iEEG). The other 10 are EEG claims or EEG against iEEG comparisons, marked `data: elsewhere` (BNCI Horizon 2020, Ofner et al. 2017).
- I checked by arithmetic that each table's Average row is the mean ± population SD of the subject rows.

**Details left open, with the readings named**
- **Neighborhood:** the Methods use the 9 nearest electrodes by projected MNI distance. The code's default is "same AAL label". I followed the Methods and named the code's choice as a variant.
- **Number of neighbors masked:** the Methods use ceil(m·|N|), the code uses round(m·|N|). Methods followed, code as a variant.
- **Mask intensity for the intra-subject, lagged and surrogate numbers:** the paper doesn't say. The figure notebook settles it as m = 1.0, so I followed that, with m = 0 as a variant.
- **Cross-subject correlation matrix:** the Methods (Eq. 3) average Pearson correlations over paired trials. The code correlates concatenated trials. Methods followed, code as a variant.
- **Phase-shuffle surrogates:** the Methods say end-matched segmentation was used; the code has none. Readings: (a) no end matching; (b) end-matched trimming.
- **iEEG trials:**
  - Which events. Readings: (a) reach onsets, 2 s centred on each; (b) movement plus rest trials.
  - Which days. Reading: all sessions pooled per subject.
  - Where preprocessing is applied. Readings: (a) on the continuous recording before epoching; (b) on each epoch.
  - Exclusions. Standard choice of none, with the code's PSD-based trial rejection as a variant.
- **Subject order:** I read table row n as AJILE12 participant n. The author is to check this against Fig. 6.
- **Settled by the code where the paper is silent:** learning rate 0.01, batch size 32, patience 200, seed 42, block length 0.5 s, and z-scoring per channel and time sample across trials.

**Missing from the paper or code**
- The iEEG trial-building pipeline. The code loads pre-made pickles. Its DANDI extraction path (one session, Hilbert envelope, 10 Hz) does not match the Methods.
- Any accession or version for the EEG dataset, and which EEG session and trials were used.
- Any statistical test. Every claim of absence or ordering (the lagged model's lack of gain, the surrogate ranking, Local above Non-local) has a rule set in this file instead.
- One finding the paper does not mention: Table II shows block shuffling above the original data for iEEG subject 3 (0.698 vs 0.535).
