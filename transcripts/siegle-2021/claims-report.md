I wrote `claims/000253/10.1038-s41586-020-03171-x.yaml`, and `tools/claims_check.py` passes it with 0 problems. But dandiset 000253 is probably not the paper's data. By its archive title and description it is the OpenScope Global/Local Oddball project (14 subjects, Neuropixels with optogenetics), recorded on the same pipeline, and it cites this paper only as "IsSupplementTo". The paper puts its 58 passive-viewing experiments in DANDI 000021 and 000022, and the Fig. 4 behaviour metrics in its GitHub repo. So 34 of the 35 claims are recorded as data `elsewhere`. Whether 000253 holds similar recordings (the same receptive-field mapping and flash stimuli, the same areas) is for the author to find.

**Text read**
- **Paper:** the NIH author manuscript in PubMed Central (PMC10399640), not the version of record. It has the main text, Methods, the Fig. 1–4 legends, the Extended Data Fig. 1–10 legends, and the data and code statements.
- **Missing:** there is no PDF, so no figure was seen. The Supplementary Information is not in the text, but the results rest on the main text, Methods and Extended Data, which are all there.
- **Code:** `AllenInstitute/neuropixels_platform_paper` at commit 4f8bcc2, plus the CCG helper `jiaxx/ccg_jitter` at 6559a4d, which the Figure 2 notebook calls. The code fixes the anatomical hierarchy scores, the unit selection, the log10 modulation index and the timescale filters; the text does not.

**Claims:** 35, all with quotes and all with criteria; 20 have expected values. 18 claims carry 27 statistics: Pearson correlations, Wilcoxon rank-sum tests (Fisher-combined across mice, or Benjamini–Hochberg corrected) and one bootstrap signed-rank test.

**Details left open, with the readings named**
- **Sharp-peak CCGs:**
  - Bin width: 1 ms, from the example in the code; the text gives no other reading.
  - CCG window: the 2 s presentation, or 3 s including the grey screen.
  - Unit quality filter: none, or the Extended Data Fig. 1j filters.
  - How the spontaneous period is cut into trials: 2 s or 3 s segments.
- **Directionality score across 25 mice:** pooled offsets, or the mean of each mouse's score. The total hierarchy score also has the area's own entry included or left out.
- **Distance control:** signed or absolute hierarchy-score difference.
- **Flash latency:** all flashes, dark only, or light only.
- **Modulation index:** mean of log10 MI (as the code does) or of raw MI.
- **Layer comparison:** difference of means or of medians; log10 or raw MI; the code's split (layer < 5, which may include layer 1) or layers 2/3 and 4 only.
- **Other counts and fractions:**
  - The 1.4% of hippocampal units with receptive fields: pooled over units, or the mean across mice.
  - Probe counts: whether 332 counts the probes of the 58 released sessions (the main reading) or of all 61 that passed quality control (a variant).
  - Baseline firing rate for the spontaneous-latency control: the rate in the grey interval, or the overall rate.
  - Gaze spread: radial, or the larger axis.
  - Hit rate and d′: averaged over sessions or over mice.
- **Decoders above chance:** mean minus s.e.m. above 0.5, or a one-sample t-test. Change modulation larger when active than passive: in every area, or in the mean over areas.
- **Exampled not identified:** the example mouse of Fig. 2d is not named, so every one of the 25 mice is a reading.

Where the Methods and the code disagree, the Methods give the main result and the code's choice is shown as a variant:
- the response decay window (0–250 ms against 40–290 ms);
- the window for the intrinsic timescale;
- the latency cutoff (250 against 500 ms);
- the jitter correction (expected value against one random resample).

**Missing for some claims**
- The change-modulation response window is not given, so that index cannot be recomputed from spikes; the claims use the paper's precomputed table.
- The behaviour sessions (hit rates, d′) have no deposit named in the paper.
- No p-values for the area pairs (Extended Data Fig. 9) or the distance-correlation values could be read, because the figures were not seen.

Nothing has been committed.
