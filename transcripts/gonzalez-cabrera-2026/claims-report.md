I wrote `claims/gonzalez-cabrera-2026.yaml` with 41 claims, and the quote checker passes with 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, flattened from bioRxiv's XML. It has the main text, the figure legends, the Methods and the legends of Supplementary Figures 1 to 4. No PDF was supplied, so I saw no figure panels, and the reference list is empty. The title in the text says "biases backward locomotion"; the registry title says "biases locomotor direction".

**Code read:** github.com/CGonzC/VTAPnO_Locomotion_Analysis at the release the paper cites (`v1.0_manuscript_submission`, commit 1ff5196). It holds the open-field tracking notebook, the photometry notebook and the MATLAB opto-tagging script. Later commits on main only add examples and reformat the code. Where the code and the Methods disagree, I followed the Methods and kept the code's choice as a variant:
- **Photometry baseline:** −1.0 to −0.1 s in the Methods, −3.0 to −0.1 s in the code.
- **Tracking filter:** the code has no likelihood filter and no gap filling.
- **Opto-tagging:** the script lacks the waveform-stability criterion.

**Counts:**
- All 41 claims have quotes; none needed an `inferred` note.
- 20 claims carry statistics (34 values the checker verified), 16 have expected values, and 40 have a criterion.
- The dataset can test 17 claims: photometry (Fig. 3a-c), acute recordings (Fig. 3d-k) and chronic recordings (Fig. 4).
- The other 24 cover the juxtacellular, tracing, slice and open-field experiments. The DANDI description does not list these. I left them at the default data setting and named in the opening comment the two Zenodo records, one cited by the paper and one by the DANDI description. Neither is said to hold raw recordings.

**Details the paper leaves open, with the readings named:**
- **Open-field per-bin tests (Fig. 2f,i):**
  - Correction: FDR (legend) or Holm (Methods).
  - Baseline: −1 to 0 s, or −1.0 to −0.1 s.
  - Time base: the legend's "light at 1–3 s" cannot be the time base, so bins are read from light onset.
- **Frequency screen (Supp. 2d):**
  - Window: 0–1 s or 1–2 s.
  - Mice: 8 (Results) or "the same three mice" (Methods).
- **Latency to peak and speed (Supp. 2e,f):**
  - Bin time stamp: bin end, centre or start.
  - Speed: all frames, gated frames or backward frames only.
  - The Supp. 2f legend's "higher" contradicts its own numbers and the Results; I followed the Results.
- **Photometry:**
  - z-score baseline and form (mean/SD or median/MAD). With the Methods baseline, Pre is 0 by construction.
  - Window measure: mean or area.
  - ANOVA with or without repeated measures.
- **Acute recordings:**
  - Onset latency is not defined (first spike, mean or median).
  - Spike width is not defined (trough to peak or half-width).
  - Firing-rate epoch: baseline epoch or whole recording.
  - auROC windows: −1 to +1.5 s (Methods) or six 0.5-s windows (Results).
  - Time-matched baseline, and paired t-test or Wilcoxon.
  - Fig. 3k: the triggering event (continuous light or tagging pulses), pooled peak or per-unit median, the subtraction baseline, and how the permutation test is built.
- **Chronic recordings:**
  - Whether the acute tagging criteria apply unchanged.
  - The FDR family (windows only, or windows and directions).
  - How units the class rules leave unclassed are counted.
  - "Response magnitude" (auROC, baseline-subtracted rate or rate ratio).
  - Normalisation of the reverse and forward PSTHs.
- **Juxtacellular recordings:** CV2 epoch, spike duration, the pinch measure (raw, change or z-score), the per-bin pinch test and the burst rule.
- **Thresholds I set:** where the paper gives no number ("many", "reliable", "sustained", "above noise"), I set a threshold and the criterion says it is not from the paper.

**Missing from the paper that claims need:**
- The number of responsive DA units behind Fig. 3j,k.
- Definitions of onset latency, spike width, burst and response magnitude.
- No code for the auROC classification, the temporal classes, the direction analysis, the 2-ms DA analysis or the statistics.
- Which LP neuron is left out of the n = 19 correlation.

The reading notes are under each claim in the file.
