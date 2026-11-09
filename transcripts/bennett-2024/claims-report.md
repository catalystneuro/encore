I wrote the claims file for DANDI:001051 at `claims/001051/10.1016-j.neuron.2024.06.015.yaml`. The quote checker passes except for one p-value. In the text, the p-value of Figure S6 prints as "p = 1.8e�6" (line 711), because the minus sign was garbled in extraction. I read it there and confirmed it is 1.8e-6. Nothing is committed.

**Text read:** the version of record, from a PDF supplied by a person. It has the main text, figure legends, STAR Methods (pages e1 to e8) and the supplement. The supplement holds only the legends of Figures S1 to S6, so its numbers are quoted from those legends. Nothing the claims need is missing from the text. The full text, Methods and supplement are all there.

**Code read:** AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit 3c09a0dc. It covers Figures 4C to 4G, 7B to 7F, 8D to 8F and the S4I counts, plus metadata tables. In the units table, receptive-field significance is p < 0.01, as the Methods say. I found no code for Figures 3, 4B (trajectories), 5, 6, S3, S4B, S4D to S4H or S6.

**Claims:**
- **Count:** 45 claims, all with quotes. 16 claims carry one statistics entry each (16 entries in all), 23 have expected values and 44 have criteria.
- **Data:** 39 claims use the dataset. 6 are `with_inputs`:
  - five compare against the 5-mm window, using the Visual Behavior Neuropixels dataset (DANDI:000713, version 0.240702.1725);
  - the MRI claim uses naive-mouse scans from Qiu et al. 2018.
- **Possibly not in the dataset:** surgery records, ISI maps, MRI, histology, training records, retraction and sharpening logs, and the optogenetics and Dura-Gel sessions. The dataset's description does not mention any of them; the author has to check.

**Details the paper leaves open, with the readings named:**
- **Alpha events** (written once in the file's header):
  - which units belong to an area: by the area's label (Methods) or by any label containing the acronym (code; for VISp this also takes VISpm, VISpl, VISpor);
  - the event rule: four maxima with three intervals of 125 to 350 ms (Methods) or the code's looser rule;
  - the random-time coherence: both areas at a random time (Methods) or the reference area at the event against the other at a random time (code);
  - the session set: the 87 sessions passing QC or all 99.
- **Pupil (Fig 7B):** pupil area (code) or diameter (text), and the mean or median change.
- **Lags (Fig 7E):** the paper's own code finds significant nonzero lags for all seven pairs (p from 2.4e-49 to 0.010). That runs against the text's "straddled zero". The claim is judged on that code test.
- **QC metrics "comparable" (Fig 4D):** the code's Mann-Whitney test or medians within 10%. The code's printed tests are significant for at least presence ratio and amplitude cutoff.
- **5-mm window yield drop (p = 6e-22):** day 1 against day 2, or the code's test across six groups.
- **RF threshold (Fig 4E):** p < 0.01 (Methods); the code's 0.05 is a variant.
- **Firing rate across days:** the text gives p = 0.21, the code and figure 0.26. Both are recorded.
- **Unit filter in Fig 8:** the Methods' presence ratio above 0.95; the code's 0.9 is a variant.
- **Fig 8 tests:** the legend's rank-sum test for 8E, with the code's signed-rank test as a variant. For 8E, "more modulated" is read on raw or baseline-normalised rates. For 8D, latency is time to peak or to half-peak.
- **Rewards across days:** all rewards, or hits only.
- **Retraction drift:** max_drift or cumulative_drift, and QC-passing or non-noise units.
- **Recovery after insertion (S4I):** the normalisation and fit for the time constant.
- **Probe entry point (trajectory consistency):** where on the probe it is taken.
- **Stimulus-offset timing (Fig 7B):** chi-square or KS test against uniform.
- **MOp against VISp frequency:** measured from inter-peak intervals or from the autocorrelogram spectrum.
- **Fig S6:** the response windows.
- **Similarity across days (Fig 4G):** taken from the paper's Kruskal-Wallis test, run on response size and on peak latency.

**Missing or inconsistent in the paper:**
- No method or code for Figure S6 (r = 0.77), the trajectory deviation, the drift-map discontinuities (judged by eye), the reward counts, or the silencing and optotagging measures.
- The failure causes the Methods list add up to 11 failed mice, against 13 in the Results.
- The code's 467 insertions over 87 sessions give 5.37 probes per session, against the 5.46 the Methods report.
- The text cites Figure 6F where it means 7F.
