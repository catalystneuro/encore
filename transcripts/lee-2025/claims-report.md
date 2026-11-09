I've written `claims/001195/10.7554-elife.105955.yaml`. The quote checker reports 0 problems: 38 claims, 38 quotes, 71 statistical values.

**Text read.** The eLife reviewed preprint, version 2 (8 July 2025): main text, Methods, figure legends and all figure supplements. I opened the PDF only for Figures 6 and 7.
- The paper links no analysis code, so every method detail comes from the Methods, legends and supplements.
- The earlier Research Square preprint uses the same patch-clamp data. I checked only its ex vivo Methods: they match the eLife text, and it adds that the cells recorded at rest came from 19 mice.
- The dandiset holds the ex vivo patch-clamp data (Figure 6) and the CeA imaging with behaviour videos (Figure 7). Those claims have full criteria.

**Counts.** 38 claims: all 38 have quotes, 27 have statistics, 22 have criteria and 16 have expected values. Of these, 20 cover Figures 6 and 7 with their supplements. The other 18 cover tracing, behaviour, RNAscope and photoinhibition, and most of them record only the paper's tests.

**Details the paper leaves open, with the readings named:**
- **EPSP/IPSP detection (6D-F, also used by 6J-K, the clusters and TTX/4AP):** no threshold is given. Readings: a deflection beyond 2 or 3 SD of the 5 s baseline.
- **Firing responses (6G-I):** how sweeps are combined is not stated. Readings: pooled intervals, or the mean over sweeps. A 5.5 s baseline (the supplement legend) is a variant of the Methods' 5 s.
- **Which cells enter 6J-K:** cells with any EPSP (or IPSP), or single-type cells only. The post hoc test in 6K is not named: Tukey or Holm-Sidak.
- **Clustering (6N-Q):**
  - Ramp ratio: absolute membrane potential, or deflection from baseline.
  - Sag steady state: last 100 ms or last 200 ms of the step.
  - Max-min normalisation, or none. The dendrogram axes (up to 200 and 350) are far above what four features scaled to 0–1 can give.
  - For capacitance the paper cites the Q-method, but its MATLAB code is not published.
- **auROC (7G-H, J, I, M):**
  - Interaction distance: nose within 0.65 or 1.3 cup diameters.
  - Head direction: from the neck or the head keypoint.
  - Time bins: 40 ms as written, or the 50 ms imaging frames.
  - Period: test only, or the whole session.
  - Mice: ChrimsonR only, or all imaged.
- **Proportion test (7J):** none is named. Readings: chi-square, or Kruskal-Wallis on per-mouse percentages.
- **Which mice enter 7M:** the counts disagree (15, 12, and 9/8/9 in different places).
- **Social time in 7E (variant):** time on the social side, or cup interaction time.
- **Functional clusters (7-S2):**
  - Linkage: MATLAB default (single), Ward or average.
  - Z-scoring: before or after averaging.
- **Combined clustering (6-S1L-N):** "very similar" is judged by my own choice of at least 80% agreement, which the criterion states as a choice.

**Missing from the paper:**
- The Figure 7 legend runs off the page in the PDF itself, so panels J to M have none. I read the 7J percentages and 7M's r = 0.679, p = 0.045 from the figure image.
- Figure 6 gives the response proportions only as unlabelled pie charts.
- The supplied text has no data or code availability statement, and the source data files are not included.
- The SLEAP model and CellReg parameters are not given; the criteria use CellReg defaults.
- 7-S1N prints r = -0.3231 with p = 0.6328 for N = 9, which do not match each other.
