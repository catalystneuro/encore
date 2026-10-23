I wrote `claims/000248/10.1038-s41593-025-02055-5.yaml`. It has 39 claims, every one with a quote and a criterion, and 21 with statistics (73 values in all). The checker passes all quotes and the schema, with one flag left: Fig. 2d's p, which the paper prints as "7.0 × 10 −6". I confirmed it by reading the legend; the checker only looks for the form "7 × 10-6". Nothing was committed.

**Text read**
- I used the version of record (Nature Neuroscience 28, 2319–2329, from Europe PMC): main text, figure legends, Methods and all ten Extended Data legends.
- The Supplementary Information (Supplementary Results and Supp. Figs 1–8) is not in `paper/` and was not read. The main findings rest on the main and Extended Data figures; the supplement is cited only in support. The one claim that rests on it (`supp3-decoder-types`) says so.
- There was no PDF. I did not use the preprint.

**Code**
- The paper's Code Ocean capsule (10.24433/CO.6659254.v2) returned HTTP 403 from here, so I could not read it.
- In its place I read the first author's GitHub repo `hs13/IC_paper_code` at commit 50e04ea. It is MATLAB and covers only the Neuropixels analysis: unit and area selection, response windows, the IC-encoder and segment responder tests, decoding, raw cross-correlograms and eye tracking.
- The cross-correlogram correction and the Fig. 2d measure come from the same author's larger repo, `hs13/Analyze_IC_OpenScope_v240130` at 4ee1585. The paper does not link it, and the file cites it as a lower source.
- I found no code for the 2p analyses or for the Fig. 1 percentages.

**Claims**
- **Neuropixels, in this dandiset (18):** Fig. 1e–g; unit counts per session; IC-encoder and segment responder counts; Fig. 2d cross-correlograms; Fig. 3a, c, d decoding; Extended Data Figs 7a–c, 6e/f and 2a/b/f/g; and the other decoder types.
- **2p imaging, holography and mesoscope (21):** Figs 1i–k, 2b/c, 3e, 4a/b, 5c–e and 6d/e, plus Extended Data Figs 3, 4, 5, 9 and 10. These are the paper's own recordings but not in this dandiset. The paper does not say where they are; its only other deposit is unnamed "additional postprocessed data" in the same Code Ocean capsule.

**Details left open, with the readings named**
- **Decoder tuning:** the code runs MATLAB's automatic hyperparameter search, which the Methods don't mention. Readings: (a) fixed defaults, linear SVM with C = 1; (b) C chosen by inner cross-validation.
- **Exclusively center-responsive units:** the Methods test each position against gray-screen trials, but the mapping block has none. Readings: (a) the code's signed-rank test against the spontaneous rate, Holm-corrected; (b) a rank-sum test against 1 s windows cut from the spontaneous block.
- **"Substantially IC/IRE-responsive" and orientation match (Fig. 1f, g):**
  - Test: (a) Kruskal–Wallis with Tukey–Kramer against blank; (b) rank-sum against blank.
  - Block: (i) ICwcfg1 only, two orientations; (ii) ICwcfg1 and ICwcfg0, four orientations.
- **"Across ICwcfg0 and ICwcfg1" (159 IC-encoders):** units that are IC-encoders in either block, or the sum of the two blocks' counts.
- **Extended Data Fig. 6b counts (87 and 636):**
  - (a) RS units in ICwcfg1;
  - (b) all units in ICwcfg1;
  - (c) RS units in the union of both blocks.
  - Fig. 2d's 79 and 526 differ from these.
- **Fig. 2d cross-correlograms:**
  - Smoothing window: 25-bin boxcar or 25 ms Gaussian.
  - Flank SD: from the raw or the corrected correlogram.
  - Per-unit measure: fraction or count of connected higher-area units.
- **"Strongest" areas (Fig. 3d):** the largest mean scores or the smallest p-values.
- **Post hoc test after Kruskal–Wallis (Extended Data Fig. 7a, c):**
  - Readings: signed-rank V1 against each area, or Tukey–Kramer.
  - Panel 7c's dataset is ambiguous (Neuropixels or 2p); this is recorded as a deviation.
- **Eye tracking:**
  - The fixed-gaze threshold is 8 degrees in the Methods and 20 camera pixels in the code; the pixel threshold is run as a variant.
  - The images in the pupil-area Friedman test: the four IC/LC images or all 22.
  - Gaze confinement has no test in the paper, so two tests are named and no pixel-to-degree conversion is applied.
- **Fig. 4a/b:** the per-subset p-values are given in figure order, so which value belongs to which subset is read from the Results text.

**Missing from the paper**
- The Supplementary Information.
- An accessible copy of the linked code.
- Any location for the 2p data.
- The figure code for the Fig. 1 percentages.
- A pixel-to-degree conversion for eye position.

The Methods also list 14 Neuropixels mice (10 Sst, 4 PV) against 12 sessions from 12 mice elsewhere in the paper; the file notes this.
