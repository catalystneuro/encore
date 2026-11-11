I checked `claims/see-2018.yaml` against the paper and made seven corrections. The file is ready for an attempt.

**Checker result:** `claims/see-2018.yaml: 31 claims, 31 quotes, 40 statistical values, 1 problems`. All 31 quotes match the text word for word. The one problem is `VALUE NOT FOUND fig10s1-random-group-strfs 8.7e-12`, and it is the checker's fault, not the file's: the paper prints the value as "8.70 x 10-12" (Supplementary file 1, row 10 - figure supplement 1E), and the checker drops the trailing zero when it searches. The 1.60e-59 value has the same issue; it passes only because of an accidental match, and it is also printed there.

**Changes, by claim:**
- **fig2eg-distance-weak:** the expected value 0.2 ± 0.13 covered 0.07 to 0.33, but the range the criterion states is 0.09 to 0.33 (10 to 30%, each bound widened by 10%). Changed to 0.21 ± 0.12.
- **fig6j-sharpness-cne-pairs:** the 15 other penetrations were one entry with the bound p < 0.001. Replaced with one entry per test, using the exact p and pair counts from Supplementary file 1.
- **fig9s2-noise-correlations:**
  - The three example recordings now have their exact p-values and pair counts.
  - The statement says cNE pairs were higher in every recording, but the criterion only tested the paired t-test across recordings. I added the per-recording Mann-Whitney U test from legend B.
- **fig9c-cne-events-more-mi:** the extrapolation step now matches the Methods exactly: 20 iterations at each of 90, 95, 97.5, 99 and 100% of time bins, with a line fitted against the inverse fraction.
- **fig7-negative-weights:** the criterion's 90% cut-off for "vast majority" is now labelled as a reading, since the paper gives no number.
- **fig11c-models-number:** applying Bonferroni across the three comparisons in the panel is now labelled as a reading, since the paper does not say which comparisons the correction covers.
- **fig11ef-coincidence-ratios:**
  - The 10-ms bin for the coincidence ratio is now stated as an assumption.
  - Which recordings the groups come from is now marked open, with two readings. The Methods take real and repeat ratios from presentations of one stimulus, which fits the 15 repeats of the 10-min stimulus, but the models are run on the 16 recordings.

Every other claim matches the paper in its statement, source, statistics and tolerances. The paper's main findings all have claims, and nothing comes from outside the paper.

**Open:**
- The paper does not fix the lag bin or lag range for the pairwise correlation functions. This affects fig2bd and the sharpness claims that build on it. The paper's 10-ms resolution cannot produce the reported ~2 ms median sharpness, so the file's 1-ms readings rest on an assumption.
- The checker's trailing-zero problem above. It is recorded under `checks`, and the file is otherwise clean.

**Ready:** yes, recorded as `ready: true` in a new `checks` entry dated 2026-11-11. Nothing is committed or pushed.
