I rewrote `claims/000582/10.1126-science.1125572.yaml` from the full text. It now has 20 claims, all with quotes and criteria. The quote checker reports 0 problems.

**Text read:** the version of record (Science 312:758) and its supplement, which has the Materials and Methods, figs. S1 to S9 and table S1. Nothing the claims needed was missing. Table S1's numbers came out of the extracted text without the table layout, so I placed them using the paper's totals and percentages, which all agree. The paper links no code, so none was read.

**Claims:**
- **Kept ids:** `layer2-grid` now uses the paper's own grid-cell criterion (gridness above 0) and the per-layer counts from table S1A. `deep-hd-conjunctive` now has the conjunctive proportions per layer and the two chi-square tests. `speed` no longer lists P < 0.001 as a statistic, because it is the threshold used to count cells, not a result.
- **17 new claims:**
  - Grid cells: present in all layers, gridness range similar across layers, stable within and between trials.
  - Spacing and field size along the dorsoventral axis, and grid phase and orientation.
  - Head-direction cells: counts per layer, recorded together with grid cells, tuning breadth across layers, full range of directions, spread of directions within an ensemble, stability across trials.
  - The continuous spread between grid and head-direction properties, conjunctive tuning matching pure head-direction tuning, and the coherent response to cue-card rotation.
  - Speed: steeper slopes for grid and conjunctive cells, and positive intercepts with rates at low speed.
- **Statistics:** 12 entries across 8 claims. Two of them are absence tests whose test the paper does not name.
- The opening comment records what changed and why, and describes the data.

**Details the paper leaves open, with the readings named:**
- **Throughout:**
  - Whether maps are built from the two trials pooled or from each trial.
  - Autocorrelogram pixel size: the rate maps use 3 cm bins but peaks are counted in 1.5 cm pixels.
  - The radius of the gridness circle and how the central peak is removed.
  - The significance level for the head-direction criteria (0.05 or 0.01).
- **Tests the paper does not name:** gridness range across layers (Mann-Whitney or Kruskal-Wallis), tuning breadth across layers (ANOVA or Kruskal-Wallis), conjunctive against pure head-direction tuning (t-test or Mann-Whitney), and the "no difference between layers" for spacing (Fisher z or a layer-by-distance interaction).
- **Measures the paper does not define:**
  - Field size: the autocorrelogram's central peak, or rate-map fields above 20% of peak.
  - Within-trial stability: half against half, or odd against even minutes.
  - The thresholds for phase offset and orientation consistency.
  - Coverage of the full direction range: 30, 60 or 90 degree sectors.
  - What the 0.84 circular correlation correlates.
  - The colocalization unit: session or tetrode.
  - How rotation is measured and how close counts as coherent in the cue-card claim.
  - How the 1.5 to 2 spacing ratio is formed.
- **Speed analysis:** path length or displacement per 1-s bin, smoothed or raw positions, and slope, Pearson or Spearman significance. For the rates at low speed: mean per cell or over pooled bins. The paper also does not say whether its ± values are SEM or SD.
- Some thresholds in the criteria are my standard choices, not the paper's (the orientation test, the phase-offset thresholds, the gap rule for continuity, the rotation tolerances). Each is labelled as such in the file.

**Inconsistencies in the paper, noted in the claims:**
- **Chi-square:** the table S1B counts do not reproduce the paper's χ²(3) = 28.4 or χ²(2) = 6.2 under either obvious table. I got 49.3 and 15.0 for conjunctive against other grid cells, and 29.0 and 16.7 against all cells. Both readings are named.
- **Degrees of freedom:** F(2,422) does not fit 423 cells in three groups, which allows 420.
- **Rat counts:** the Histology section says 16 rats, the rest of the paper says 17.
- **Cell counts:** fig. S4 says 388 cells for layers III to VI, the main text says 385.

**What the dataset may not support:** its description says it holds spike times of grid cells only, a sample of the paper's data. If so, the layer proportions in `layer2-grid`, `hd-layers` and `deep-hd-conjunctive` cannot be tested, since they need every sorted cell. The spacing and field-size claims need each recording site's distance from the postrhinal border.
