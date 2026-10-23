I wrote `claims/000019/10.1038-nature11911.yaml` with 22 claims. The quote checker passes with 0 problems. Nothing was committed.

**Text read.** The NIH author manuscript from PubMed Central (PMC3606666, NIHMS436351), which is not the version of record. It includes the main text, figure legends and Methods, plus the full supplement: Supplementary Figures 1 to 13 with legends, Supplementary Table 1 and the Supplementary Methods. There was no PDF of the main text, so the main figures were read from their legends and from the Results sentences that cite them. To view supplement pages 2 and 8, I installed PyMuPDF into a temporary directory. The paper links no code.

**Counts.** 22 claims, all with a quote and a criterion. 11 record statistics (17 values), and 13 have expected values with tolerances. Every claim uses the dataset alone; the paper relies on no outside data.

**Details the paper leaves open, with the readings named:**
- **Baseline for the high-gamma z-score:** (a) a silent window before each utterance, (b) statistics of the channel's whole recording.
- **"Change in z-score > 2":** (a) above 2, (b) absolute value above 2.
- **Figure 1 electrodes (e124 and the others):** the subject is unnamed, and the numbering could start from 1 or from 0. The activity measure is either the response at -25 ms or the peak over the epoch.
- **Labial/coronal/dorsal labels for /h/ and /r/:** (a) both left out, (b) /r/ coronal and /h/ dorsal.
- **Supplementary Figure 3 cross-correlations:** normalisation is either Pearson correlation over the overlap or scaling by the zero-shift value. The diagonal is either at 45° or along the anisotropy axis. The map grid is 1 mm, with 0.5 mm as a variant.
- **Supplementary Figure 5:** pairs are formed either within subjects or pooled. The linear-somatotopy null is never described (the legend says "see Methods" and the Methods are silent), so the legend's own bounding values are used.
- **Partial-correlation timing (Fig. 3d):** the threshold is computed either per articulator or over all articulators. Onset and offset are either threshold crossings or half the peak. The ANOVA is either on onsets or on peaks.
- **R² onset latency (Supplementary Figure 7):** either the first significant time or the 2.5 SD rule. The guenon boundary comes from the dataset's anatomical labels.
- **Time range for PCA:** -500 to 750 ms, or -375 to 620 ms.
- **Clusters for separability:** phonetic groups, or k-means at each time. The separability onset is either a 2 bootstrap s.e. rise or half the peak.
- **Feature set paired with separability (Fig. 5d):** constriction location or vowel configuration, or the mean of the feature sets.
- **Consonant–vowel distance pairing:** either the mean of the two cross pairings or i at the consonant time with j at the vowel time.
- **n = 297** is read as 99 time points × 3 subjects; which end point is dropped is open.
- **n = 4623** is read as the syllable pairs within subjects (1596 + 1596 + 1431).
- **Supplementary Figure 9:** whether the electrodes are all 266 or only the significant ones.
- **Smaller gaps:**
  - Fig. 4c–d does not say whether it shows one subject or several, so each subject is run.
  - The paper gives no purity measure for the hierarchy, so I set a two-thirds majority rule. That threshold is my choice, flagged as open in the claim.
  - The filter-bank centres are not given; the cited Mesgarani and Chang (2012) bank is the standard choice.

**Missing or flawed in the paper:**
- The articulator matrix (Supplementary Figure 1d) and the phonetic feature matrix (Supplementary Figure 12) exist only as images. They are cited for the author, not transcribed.
- The Methods cite the wrong supplementary figures in places (Supplemental Figure 6 for the eigenvalues, which are Supplementary Figure 8; Supplemental Figure 9 for the feature matrix, which is Supplementary Figure 12). The claims note this.
- Supplementary Figure 5 prints "P >10-3" although its *** marks mean significance. It is recorded as printed, with a note.
- Fig. 1f–h gives only qualitative examples at unnamed electrodes. Only its /ju/ dorsal-electrode part is judged; the rest is shown, not judged.
- The spatial claims need electrode positions relative to the central sulcus and Sylvian fissure. If the dataset lacks them, those claims are blocked.
