I wrote `claims/dana-2016.yaml` and did not commit it. The quote checker reports 35 claims, 35 quotes, 15 statistical values and 0 problems.

**Text read:** the version of record (PMC4846379), as flattened text: main text, Materials and methods, and all figure, figure-supplement, video and source-data legends. Supplementary files 1 and 2 are the culture screening tables; I read their column headings and the rows for the named sensors. There is no PDF, and no claim needed a figure. The paper links no code. The data set's own Figure 4 script (`data_analysis_for_CRCNS_jRGECO1a.m`, named in the data description) is one of its files, so I did not read it. The criteria say that where it settles an open reading, its choice is the main one, and that the Methods win where the two disagree.

**Claims:**
- **Testable on cai-2 (8):** the Figure 4 claims. They cover the number of cells and mice, the event counts per AP bin, jRGECO1a detection of 1 AP (82%) and 2 APs (96%), jRCaMP1a detection (65% and 80%), jRGECO1a above jRCaMP1a in ΔF/F0 and d′ for 1 to 8 APs, and faster jRGECO1a kinetics.
- **One more Figure 4 claim** (kinetics similar to GCaMP6f and GCaMP6s) is `data: elsewhere`, because the GCaMP6 values come from Chen et al. 2013b.
- **Three claims** are `data: elsewhere` on the supplementary tables: the screen counts (353 of 934 and 187 of 689) and the 8.5-, 24- and 13-fold culture improvements.
- **The other 23** rest on recordings that cai-2 does not hold: culture and protein experiments, V1 grating imaging, lysosomes, 900 nm excitation, imaging depth, L6, dual colour, fly, zebrafish and worm.
- 21 claims have `statistics` (15 p-values checked), 32 have `expected` values, and 32 have a `criterion`.

**Details the paper leaves open, and the readings named:**
1. **Trace segment projected for templates and ROC:** (a) from the first AP to the noise-bin length (4 s for jRGECO1a, 5 s for jRCaMP1a); (b) the same with the 10 baseline frames added; (c) from the first AP to 1 s after it.
2. **Templates:** (i) built from all events, as described; (ii) leave-one-out.
3. **"Accuracy (5% false-positive rate)":** read as the hit rate above the 95th percentile of the noise projections. Balanced accuracy is shown only as a variant.
4. **Event isolation for n APs:** more than 1 s (a) before and after the event, or (b) before only. Noise bins are (i) consecutive, or (ii) also kept 1 s away from spikes.
5. **Window for peak ΔF/F0:** up to 1 s after the first spike, or the projected segment.
6. **Kinetics:** half decay is either the fitted time constant × ln 2 or the time from peak to half peak. Half rise is not defined; I read it as the time from the first spike to half of the peak. "Small fitting error" is read as the 16 traces with the lowest RMS residual.
7. **Thresholds I chose because the paper gives none:** a 25% bound for "stable" (long-term expression) and for "similar to GCaMP6", a 0.8 to 1.25 ratio (or screen p ≥ 0.01) for "similar" decay in culture, and a 10-pulse to 5-pulse ratio below 2 for "partially saturated" in zebrafish. Each one is labelled in its claim as a choice made here.

**Missing from the paper:** the tables of Figure 2 source data 1 (purified-protein properties) and Figure 7 source data 1 to 3 (fly NMJ summaries) are not in the text, only their legends. No claim rests on a number found only there. Figure 4g gives its rise and decay times only in the figure, so that claim is judged by direction alone (jRGECO1a faster on both).
