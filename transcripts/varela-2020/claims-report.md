I wrote the claims file at `claims/crcns-hc-24/10.7554-elife.48881.yaml`. The quote checker passes: 46 claims, 46 quotes, 69 statistical values, 0 problems. Nothing is committed.

**Text read**
- I read the version of record (PMC7319772, Europe PMC full-text XML), including the Results, all figure legends, the figure supplement legends for Figures 1 to 7, Table 1 and the Methods. There is no separate supplementary file. I did not open the PDF.
- The data descriptor told me what the dataset is meant to hold: three rest sessions from three rats, with event timestamps derived by the authors. It mentions no maze sessions.

**Code**
- The paper links no analysis code. Its only software link is Xclust, the spike-sorting program, which fixes no analysis choice, so I did not read it.
- The Matlab scripts the paper mentions are files inside the CRCNS deposit, so I left them alone. No method detail comes from code.

**Counts**
- 46 claims, all with quotes and none marked `inferred`.
- 28 have statistics, 32 have expected values, and all 46 have criteria.
- All use the paper's own recordings; the paper uses no outside data.
- Covered: the timing and phase links between SWRs, KCs and spindles; thalamic firing rate and bursting; thalamic firing around SWRs and the GLMs; the thalamic rebound after KCs and the asymmetry index; autocorrelations and pair cross-correlations; phase-locking; the modulation index against ripple power and spindle amplitude; SWRs coupled and uncoupled to spindles; and the maze and CA1 "run unit" findings.

**Details the paper leaves open, with the readings named**
- **Sleep periods:** the moving-average window is not given and periods were confirmed by eye. Readings: the deposited sleep periods, or the stated rule with a 1 s or a 10 s window.
- **Detection thresholds, where the Methods and Results disagree:**
  - SWRs: 3 sd in the Methods, 4 sd in the Results. Readings: 3 sd, 4 sd, or the deposited timestamps.
  - Spindle troughs: filtered-trace minima in the Methods, a squared-trace threshold in the Results. Readings: both, plus the deposited timestamps.
  - KCs: the mean and sd come from sleep periods or from all immobile time.
- **Which LFP wire was used** (chosen by eye in the paper).
- **"Waking"** is undefined: all time outside sleep, or time above a velocity threshold the paper does not give.
- **Peri-event windows:** a cell or tetrode counts by either the minimum or maximum bin beyond 2 sd, or the mean over the window.
- **The SWR shift control:** the range of the random shift is not given.
- **The GLM:**
  - the predictor is unit spikes (as the Results say) or tetrode multi-unit spikes (as the Methods say);
  - firing is in spikes/s or in counts per 250 ms bin;
  - the 61.7% counts units negative for SWR counts, for CA1 multi-unit spikes, or for either.
- **Autocorrelations:** bin size of 5 or 10 ms, and a spindle band in lags of 71 to 167 ms or 50 to 150 ms.
- **Pair cross-correlogram z-score:** against the correlogram itself or against a shift null.
- **Phase-locking:** how the baseline normalization enters the Rayleigh test. The 67.74% counts units that are significant, units with a positive mean phase, or both.
- **The asymmetry index:** which histogram (raw rate or z-scored) and which normalization (the larger maximum or the sum of the two).
- **Spindle-cycle measures:**
  - cycle amplitude is the mean of the two peaks or the larger one;
  - in the quartile analyses, the median used for the split and what the quartile is compared with are not given.
- **Tests the paper does not name:**
  - RE against other nuclei: Fisher exact or chi-square;
  - the claim that spike counts do not change: Wilcoxon signed rank, following the Methods' rule for paired data.
- **Unpublished thresholds:**
  - "run" CA1 units were classified by eye: any labels the dataset gives, at least 50 spikes on the maze, or any spike on the maze;
  - which spikes count as "in" an SWR is not defined;
  - the co-modulated CA1 pairs were chosen by eye.

**Missing from the paper or limiting a claim**
- One value is printed as "−64 ± 1.42" (the coupled thalamic multi-unit z-score). It is almost certainly −0.64; I recorded no expected value for it.
- The rule behind each unit subset (n = 40, 47 or 31 units, 39 pairs) is not given, so criteria run on all eligible units and report n.
- In the no-maze control sessions, n = 4 means the paper's test can never reach p < 0.05, so the criterion says how that claim is judged instead.
- The maze claims need the six maze sessions, which the data description does not list.
