I've written the claims file for EBRAINS:Q0FG-1X8: `claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml`.

**Text read.** I read the version of record (PDF supplied by a person) as extracted to `paper/…txt`: main text, figure legends, STAR Methods, Supplementary Figures 1 to 8 and Supplementary Table 1. Three things had to come from the PDF instead:
- The Supplementary Figure 7 legend is an image and is missing from the text. I read it from PDF page 46.
- The CA3 p-values in Supplementary Figure 3F came from PDF page 35.
- Supplementary Table 1 is garbled in the text and some exponents are lost, so I used it only where it is legible.

**Code read.** The paper's code is on Zenodo (doi:10.5281/zenodo.7797252), a copy of GitHub sebasoa/Object-centered-population-coding at v1.0, commit 4e4f5ac. It holds the object-tuning score and the distance decoder. Two functions they call are not in the repository: `objectScore` and `PoissonDecoder_distance`. The steps they would do are taken from the Methods. There is no code for the single-cell change analyses, traces, words and counts, mutual information, KL divergence, the behavioural decoders or the population vector correlations.

**Claims.** There are 55 claims and all 55 have a quote that the checker found. 38 claims carry statistics (68 entries), 17 have expected values, and all 55 have a criterion. None needs data from outside the dataset. The checker still exits non-zero, with 28 problems: all are p-values it could not match, either because their exponents are garbled in the text or because they sit in the image-only Supplementary Figure 7 legend. I checked each one by reading.

**Details the paper leaves open, and the readings named:**
- **Template width:** standard deviations of 5 to 200 cm (code), or variances of those values (Methods).
- **Speed filter in the decoder:** rate maps from epochs above 2.5 cm/s (Methods), or no filter (code).
- **Which sessions are decoded:** the Methods' rule of at least 25 cells, which the text says gives 17 sessions, against the 16 the legends give. The second reading runs every set of 16 that drops one tetrode session.
- **Which session stands for a cell recorded on several days:** the first day, or every session.
- **Which control trials stand for O and OM (chance level):** CON2 and CON3, or CON1 and CON2.
- **Field distance:** the centroid in O, the centroid averaged over O and OM, or the peak bin.
- **Cross-day count:** 13 (text) or 11 (Fig 1H legend).
- **Trace ROI size:** the Methods cite a section that is not in the paper. Readings are a circle of the field's area, or the smallest circle containing the field.
- **How traces were removed (Fig S2D):** only one reading is named.
- **Object-vector map bins:** taken from the paper's references 11 and 12.
- **Population vector correlation bins:** fixed 20 cm rings, or equal-count bins (which the reported 489 values per bin implies).
- **Angular sector origin:** 0 or 36 degrees.
- **Control-session object position:** (75, 75) or (35, 120) cm.
- **Figure 3D data:** the 620-cell session (Methods) or four datasets pooled (legend).
- **Figure 6C:** three different lists of subset sizes, and the test is either signed-rank or Kruskal-Wallis, since the printed W values are not integers.
- **Neuropixels word subsets:** one subset of 30 cells, or the mean over 20.
- **Words against counts:** compared per distance bin or pooled. The printed U ≥ 439 fits neither.
- **KL divergence:** the paper does not say how words that never occur in O were handled; the sum is restricted to words seen in both trials, recorded as a deviation.
- **Entropy:** the unit it is computed over, and whether the all-zero word is included.
- **Downsampled words:** with or without the bias subtraction.
- **Single-cell analyses:** all 1,189 cells, or only the cells of the decoding sessions.
- **Random partition:** 1 s bins or position samples.
- **Behaviour matching:** done on 1 s samples or on 25 Hz samples.

**Choices made where the paper is silent:**
- **Lowess span:** 0.5 s, treated as unable to change the result.
- **Signed-rank pairing in the change classification:** pairs matched by repetition.
- **Tolerances that are not 10%:**
  - 0.05 on the Fig 7 correlation coefficients.
  - 0.005 on the single-cell mean of 0.02.
  - The legend's SD for the shuffled-label accuracies.
- **Tests chosen where the paper gives none:** Figs 1F, 3B to 3D, 4C and S5G to S5I. Each follows the paper's general tests or its own measures.

**Missing from the paper:**
- The ROI section the Methods refer to.
- The method for removing traces.
- The two code functions named above.
- The Supplementary Figure 7 legend in the text.

**Inconsistencies in the paper,** noted in the opening comment:
- 13 against 11 stable cells.
- Identical statistics printed for OM-NO' and NO-NO'.
- 12.2% against 12.3% of cells with positive distance tuning.
- 15 against 14 tetrode sessions.

Nothing was committed. The other untracked files at the repository root were already there; they are not from this run.
