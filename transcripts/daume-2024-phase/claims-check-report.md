The checks entry marks the file `ready: true`. Final checker result: `57 claims, 57 quotes, 117 statistical values, 0 problems`. The first run, before my edits, had 56 claims and 0 problems.

**Changes, by claim**
- **cohort-counts**: added the reason for the zero tolerance: these are counts of recordings the dataset should hold, not estimates.
- **fig2c-no-load-effect-other-areas**: the pre-SMA and dACC tests are now marked FDR corrected over five areas, as the Fig. 2c legend says.
- **tables1-slow-fast-theta**: the criterion counted 20 area and band tests. Table S1 has 19, because pre-SMA had no channel for fast theta to high gamma.
- **edf3-hippocampus-pac-controls**:
  - The paper does not say how power was estimated. This is now named as open, with two readings (Hilbert amplitude and Welch spectrum).
  - The preferred-phase test (panel g) had been given as a V test, which the paper does not name. It is now open, with two readings.
- **edf4b-persistent-activity-by-area**: added the four tests against baseline for hippocampus and amygdala (p = 0.0001). The criterion used them but the statistics list left them out.
- **edf7a-pac-neurons-no-category-decoding**: the 0.2 to 1.0 s rate window had been stated as fixed, but the paper only says "during picture presentation". It is now open: 0.2 to 1.0 s, or 0 to 2 s.
- **fig5b-hippocampus-vmpfc-theta-sfc-load**: the cluster window "2 to 8 Hz" was invented. The criterion now asks for a cluster overlapping the paper's theta band (3 to 7 Hz) and cites the reported 2.5 to 4.3 Hz.
- **fig5cd-no-effect-category-amygdala**: the statement now also covers the Results' "or regions" for amygdala PAC neurons, which the criterion already tested.
- **fig6d-removing-pac-neurons**: the paper corrects "for all comparisons" without listing them. That is now open, with two readings: the four tests of 6d, or those plus the two of 6e.
- **edf8fgh-frontal-controls**: new claim for Extended Data Fig. 8f-h, the frontal control analyses the Results cite. It is a claim of absence.

**Open, recorded in `checks`**
- **fig4-amygdala-pac-neurons**: the paper is inconsistent. It gives n = 156 neurons but t156, which implies 157. The file keeps 156.
- The paper's code repository was not available in this run. The details the file attributes to it could not be checked (median RT per session, the post hoc threshold in category selection, the GLM phase-bin edges, the epoch length, the angle function).
- The cluster tests use FieldTrip's default cluster-forming threshold and cluster statistic, which the paper does not state.

The rest of the file matched the paper: statements, sources, statistics (results, not selection thresholds), tolerances, and the general rules G1 to G4 and open details O1 to O11. Every claim comes from this paper. Nothing was committed or pushed.
