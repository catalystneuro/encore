I've written the claims file at `claims/000462/10.1038-s41467-022-34465-5.yaml`. The quote checker reports 41 claims, 41 quotes and 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (PMC9636178, from Europe PMC): main text, figure legends and Methods.
- **Supplement:** Supplementary Information (Supplementary Figs. 1 to 21 and their legends), plus the peer review file and the reporting summary.
- **Not available:** there is no PDF of the main article, so p-values printed only inside the main figure panels could not be read. The Source Data file is not under `paper/`.
- **Code:** github.com/seethakris/HPCrewardpaper at commit 5b3b22a. It covers behaviour (licking, lick stop, engagement, pupil), the Bayes decoder, population-vector and k-means analysis, and the VTA axon ramp scripts in MATLAB.
- **Not in the code:** place field detection, the place field measures (reliability, out/in ratio, width, intensity), spatial correlation, the place field fate analysis and the reward cell definition. The scripts load these from precomputed MATLAB files, so those criteria rest on the Methods alone.

**Counts**
- 41 claims, all with quotes, all with criteria, 30 with expected values.
- 19 claims carry statistics, 60 entries in all. Most are 95% CIs from the text. The p-values are P = 0.06, 0.14 and 0.7, and the thresholds p < 0.01 and p < 0.001.
- The claims cover Figures 1 to 5 and Supplementary Figs. 1 to 21.
- The dandiset description lists only the WT extinction data (Figs. 1 to 3) and the DREADD data (Fig. 4). It does not mention the axon imaging (Fig. 5), the dark controls or pupil video, so those claims may not be testable on this dataset.

**Details the paper leaves open, and the readings named**
- **Lick stop lap:** three readings, one lap apart.
  - L1: the first of the two no-lick laps (the code).
  - L2: the second of them (Supplementary Fig. 4 legend).
  - L3: the lap after the two (the Methods sentence read literally).
  - Code variant: it counts licks over the whole lap, not just the reward zone.
- **Decoder:**
  - Training: the Methods' first 60% of R laps is the main reading; the code's first 50% of R frames is a variant.
  - Which laps go into each mouse's mean: the Methods don't say, so I followed the code (a resampled 4 or 3 laps per condition). All laps is the variant.
  - Bonferroni correction or not: both are run and must agree.
- **Engaged laps:** the Methods print the threshold as "mean ± 1.5 SD". I read it as mean − 1.5 SD, as the code does. The code also computes the approach ratio differently from the Methods; that is a variant.
- **Pupil engagement threshold:** the paper gives it three ways (P1 Results, P2 Methods, P3 Supplementary Fig. 6 legend).
- **Within-R reference for spatial correlation:** control mice (S1) or the two halves of R in the same mice (S2). The legend's "paired" test fits neither. Both are run and must agree.
- **Place field fates:** "stable" versus "remapped" is not defined anywhere. Readings F1 to F3 cover overlap of field extents, COM inside the earlier field, and same position group.
- **Means:** per-mouse versus all fields pooled, for the place field measures and the medians.
- **Lap speed units:** the paper prints m/s; the values (about 42) only make sense as cm/s.
- **Saline slow-lap split:** the legend says after-saline laps "above the 40th percentile", which contradicts "slower laps"; both readings are run.
- **Reward cell window:** 2 s in the Methods, 1.5 s in the legend.
- **Per-position KS test in Fig. 4:** whether it compares with saline or with the R/RE low pair.
- **Unnamed tests:** the two tests behind P = 0.14 and P = 0.7.
- **Fixed by me before any analysis:** start, middle and end of the track are taken from the Figure 5d legend. Several thresholds for findings stated only in words are mine and marked "fixed here" in the criteria (for example 9 of 12 mice, 0.2 and 0.3, "less than half").

**Missing from the paper that a claim needed**
- The p-values in the main figure panels (no main PDF).
- The place field and reward cell code.
- The baseline and significant-transient method, which the paper takes from refs. 44, 67 and 75 without restating it.
- The definitions of the place field fates.
- The time bins used for reward cells.
