I wrote the claims file at `claims/001539/10.7554-elife.79545.yaml`. The quote checker passes every quote. It flags one value it cannot match: p = 1.80e-4 in `fig2d-beta-power-increase`, which the paper prints as "p=1.80e-4" (with the trailing zero), so I confirmed it by reading.

**Text read.** The version of record (eLife, PMC9799972.1, via Europe PMC): Results, every figure and figure-supplement legend, Methods, and the code and data statements. The only supplementary file is a table of cell counts per session that is not in the text; no claim rests on it. No PDF was supplied, so I saw no figures.

**Code read.** JadhavLab/Jadhav-Lab-Codes-JHB at 88d5f8d2bb39796b8656dc42bd42969a7bbe8697 (BetaOdorProject). It holds two pipelines that often disagree: Symanski's (`figures1-6Functions`) and Bladon's revision code (`figure7Functions`). Nothing says which one made each panel, so where they differ I named both as readings. The paper also deposited processed data on figshare (doi:10.6084/m9.figshare.19620783.v1); no claim needs it.

**Counts.** 47 claims, all 47 with quotes, 101 statistical values. 46 claims have criteria; `fig1b-performance` has no statistics. All claims use `data: dataset`.

**Details the paper leaves open, and the readings named:**
- **LFP power and coherence:** reading A uses time-matched pre-odor windows, the whole sampling period, and all tetrodes averaged. Reading B uses fixed 500 ms windows and the tetrode with the most units. Taper settings differ between them.
- **Cell types:** the Methods give 7 Hz and 0.3 ms. Open are whether the firing rate is over run epochs or all epochs, and whether width is trough-to-peak or half-width. The code's 8.5 Hz and 9.5 Hz thresholds are variants.
- **Unit selection:**
  - Active units: at least 100 spikes in any one epoch, or summed over run epochs.
  - Task-responsive cells: all completed trials, or correct trials only.
  - Phase locking: a minimum of more than 10 spikes, or more than 5.
- **Incorrect-trial selectivity index:** rates over the whole sampling period, or the code's 50 ms bins averaged from 0.2 to 1 s.
- **Cross-correlograms:** spikes from the whole sampling period or its last 0.5 s; peak significance one-sided or two-sided.
- **Cross-region locking:** chance level 0.0167 or 0.05 for the binomial test.
- **PCA:**
  - Cells: pyramidal only, or pyramidal plus interneurons.
  - Fit: on trial-averaged bins, or per bin on single trials.
  - Null bound: 95th or 97.5th percentile.
- **GLM:**
  - Windows: aligned to odor onset (Methods) or to port exit (code), since the Results report time before exit.
  - Link function: log (Methods) or logit (code).
- **Other analysis windows:**
  - SWR windows: beam-break periods, or the code's speed-defined stops.
  - Phase offsets: whole sampling period or last 500 ms.
  - Theta shift: the code's split 0.8 s after odor onset, or odor sampling against running.
- **Decoders and spatial:**
  - Decoder cells: task-responsive cells, or all units active on at least 10 trials.
  - "Spatially active" ensembles: cells with place fields, or cells firing during runs.
  - Full-maze sessions: 6 rats (Results) or 5 (Methods); both sets are run.
- **Smaller points:**
  - Coupling: one pooled measure or per session.
  - Behavior: whether trials under 0.5 s count toward performance; how the 95.4% turn match is averaged.

**Where the paper disagrees with itself (recorded as readings):**
- The Results say the anti-correlation in non-selective cells (Fig 3–S1e) is not significant; the legend gives r = -0.34 with p < 0.01.
- Interneuron counts are 83 and 28 in the Results but 96 and 36 in the Fig 5c legend.
- For Fig 5–S2, the Results give p = 0.0023 and the legend p = 0.0031.
- The Fig 2–S2d legend says CA1 RR leads OB, and also that no consistent RR offset exists between OB and CA1.
- For correct against incorrect trials, the Results name a signed-rank test and the legend a rank-sum. That claim is reproduced only if both tests agree; if they differ it is blocked as methods_underspecified.
- The Methods' bootstrap p-value for Fig 2g counts in a direction that would give p near 1 for the reported effect, so the lower tail is used.

**Missing from the paper or its code:**
- No code was found for Fig 3–S1c or for the resampled-pyramidal control in the GLM.
- No sniff-detection rule is given, and the code's peak finder is missing from the repository.
- The trajectory-selectivity shuffle in the Methods has no counterpart in the code.
- Several helper functions are missing from the repository (`event_spikes`, `nFoldBayesPoisson`, the filter files).
- No figure could be seen, so the directions in Fig 2d (middle) and Fig 3–S1c are left for the attempt to report.

Nothing a claim needed was missing outright, so every claim could be written.
