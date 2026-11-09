I wrote `claims/000013/10.7554-elife.06619.yaml` with 44 claims. The checker passes the schema and every quote, but it exits non-zero on two p-values it can't match. The paper prints them with a trailing zero ("p = 2.30e-5", "p = 1.0e-5"), and I confirmed both against the text by reading. Nothing is committed.

**Text read:** the version of record (PMC4525079, from Europe PMC). It has the main text, Methods, Table 1, every figure and figure-supplement legend, the decision letter and the author response. eLife has no supplement beyond the figure supplements, whose legends are in the text. There was no PDF, so I read no figure images. One Table 1 cell is garbled (L5 "24.0–18.6%"); I read it as 24.0 ± 18.6% from the Results.

**Code:** the paper links github.com/hireslab/HLab_Whiskers, read at commit cdbc914 (2020); the last commit before publication is 0eb360a. It holds only whisker-tracking post-processing, contact detection and data classes. None of the paper's analyses are in it, so it settles no criterion.

**Counts:**
- 44 claims; 41 have quotes and 3 (the Table 1 rows) are marked `inferred`.
- 11 claims carry statistics, 16 entries in all: Wilcoxon rank-sum and signed-rank tests, and correlations.
- All 44 have criteria. All use the dataset's own data.

**Details the paper leaves open, and the readings named:**
- **The example cell is not identified.** I take it as the L4 C2 cell matching 0.73 → 1.91 spikes/s and FF 7.51. Two sets of numbers could be that cell or the population: "1.51/0.31 spikes per touch, 8 ms" and "0.67/0.23 spikes/s while whisking / not whisking". For each, the readings are the example cell, the L4 C2 mean, the median, and (for the rates) all spikes pooled.
- **Trials used:** all trials, or the "performing trials analyzed". **Sample-epoch range:** over trials or over session means.
- **Whisking bouts:** whether peak-to-peak is twice the Hilbert amplitude or the range of theta within a cycle, and whether touches break a bout.
- **Touch latency:** which PCTH (first touches or all touches) and how far after onset to search. The legend contradicts itself on L5 latencies, so L5 is not judged there.
- **Touch-coupled spikes (Figure 3):** how spike times are shuffled (uniform, or circular shift), "closest touch onset" (before the spike, or either side), and whether the phase window is ±t_w or t_w wide.
- **Decoders (Figure 4):**
  - What the "non-touch" epochs are, and the detection measure (hit rate, or percent correct).
  - The timing "uncertainty": RMS error, half-width of the 95% bound, or 1.96 × RMS.
  - The phase-decoder likelihood and how the shifts are drawn.
- **Figure 5:** the velocity window and the curvature window, how ties in touch order are binned, and what the correlations are taken over. Across the 31 cells' modulation indices fits the reported p-values; pooled tuning curves is the other reading.
- **Figure 6:**
  - OPTICS parameters, and whether the inter-contact interval runs from the previous touch's onset or offset.
  - Which minimum Fano factor counts: per group, or across the five groups.
  - What "close to the binomial limit" means: the limit inside the resampling interval, or nearer the limit than to 1.
  - How the data and the refractory-Poisson model are compared.
  - Which touches feed the Figure 6E conditions, where the random windows are drawn, and the range of sliding-window starts.
- **No alpha is stated** for the claims of no difference. I used 0.05, which fits the p-values the paper calls significant.

**Inconsistencies in the paper:** for L4 outside C2, the touch-evoked spike fraction is 8.4 ± 13.3% in the Results and 9.2 ± 13.7% in Table 1. Both are recorded.

**Missing:** nothing a claim needed. The text is complete.
