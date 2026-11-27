I wrote `claims/elliott-2026.yaml` with 23 claims, and the quote checker reports 0 problems. Nothing the claims needed was missing from the paper text.

**What I read**
- **Text:** the accepted author manuscript from PubMed Central (PMC12931417). The file header calls it the version of record. It includes the main text, Methods, figure legends and the Code and Data Availability statements.
- **Supplement:** Extended_Data.pdf (Extended Data Figs. 1 to 13 and Tables 1 to 4). Tables 1 to 4 and the connection counts in Extended Data Fig. 10 are images in the PDF, so I read those pages from the PDF itself. I did not watch the videos.
- **Code:** github.com/braingeneers/human_hippocampus at commit 0f83f70. Its saved outputs match the paper: 784 significant pairs and p = 9.66e-20 for S1, and 70 of 212 and 101 of 180 phase-locked units.
- **Dataset:** DANDI 001132 holds the raw recordings from Andrews et al. 2024. The curated spike sortings the paper analysed are only in the GitHub repo.

**Claims**
- All 23 have a criterion. 21 have quotes, and 2 are marked `inferred` because their numbers appear only in Extended Data Tables 1 and 2.
- 10 have expected values and 2 have statistics: the Kuiper p = 0.01 and the geometry t-test p < 1e-19.
- By data source: 18 are `with_inputs` because they need the GitHub sortings, 4 use the dataset alone (the LFP and theta claims), and 1 is `elsewhere` (the simulation code).

**Details the code settles, where the Methods are silent**
- **Circuit pairs:** STTC window 20 ms, pairs flipped to point in the direction of positive mean latency.
- **Geometry test:** position is the nearest of 100 points on the fitted curve; the test is Student's t on angle ≥ 0 against angle < 0.
- **Phase locking:**
  - The LFP comes from the electrode nearest each unit.
  - The seizure and non-seizure windows are set by hand.
  - The Methods select spikes while the envelope is above its RMS, but the code selects spikes in cycles whose peak exceeds it. I followed the Methods and named the code's version as a variant.
- **STTC clustering:** entries of 0.3 or more are set to 0, with complete linkage.
- **Filters:** Butterworth order 5. The Methods also mention a fourth-order filter, so both are run.

**Details left open, with the readings named for each**
- **Bursts and superbursts:** the code has no detector. Readings are a population-rate peak above 2× the pre-KA mean, or above mean + 3 SD, at smoothing of 10 and 20 ms. The code's own S1 windows list 8 superbursts where the text says 11.
- **Firing-rate increase after KA:** compared within the KA recording (before vs after onset), against the separate baseline recording, or over the bursting period only.
- **Onset latency:** one Methods passage says within 15 s, another within 30 s. Both are accepted, and the KA application time must come from the dataset's metadata.
- **Spectrogram:** which electrodes are used is not stated. Readings are electrodes near the most active units, or electrodes spread along the layer.
- **Phase-cluster split for the Kuiper test:** the code's hand-set position thresholds, a median split, or k-means on position. No Kuiper code exists, so I specified astropy's `kuiper_two`. The text prints p = 0.01 and the legend p < 0.01; both are accepted.
- **Phase-locking span for non-KA recordings:** the whole recording, or the spans used in the code's get_raw_data notebooks.
- **STTC threshold:** values of 0.3 or more set to zero (code) or clipped at 0.3 (variant). The two clusters are cut with fcluster set to 2 clusters, or as the code cuts them.
- **Geometry test:** y-axis direction, both run. Tolerance is 10% of −log10 p.
- **"45,000 pairs":** read as 212², as the code prints it.

**Claims the paper judges by eye** (stage directions, electrode clusters, bipolar histograms, eigenvector gradient, sub-burst alternation, reconstruction error): for these I wrote measures myself and labelled them in the criteria as not from the paper.

**Weakest points**
- The rolling-wave counts come from watching videos and have no detector, so that claim is blocked as `methods_underspecified` unless a detector is adopted as an assumption.
- The S2 sub-burst times are not in the paper. They are taken from the code's notebook for S2.
- The code shows which folder is which slice except for S5 and S6. The unit counts (136 and 100) fix that match.
