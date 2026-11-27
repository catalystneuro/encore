I wrote `claims/henry-2022.yaml`. It has 31 claims, all with quotes, and the quote checker passes with 0 problems.

**Text read**
- The version of record, as extracted from the PDF: main text, STAR Methods (pages e1 to e3), and the supplement with the legends of Figures S1 to S7. Nothing the claims need is missing.
- The PDF pages could not be rendered here (no PyMuPDF or poppler), so no figure was read beyond its legend and the labels the extraction keeps.
- In Figure S7 the per-animal neuron counts only add up one way (V1 264 and 132, V4 288 and 403), but which animal is which is unread. The claims report them that way.
- The extraction garbles the tuning-model formula and its Poisson likelihood; the opening comment states how I read them.
- **Code:** the paper links none. Its data statement names only the CRCNS deposit and offers further information "upon request", so every method below comes from the Methods, legends or supplement.

**Counts**
- **Quotes:** 31 of 31; none of the claims is marked as inferred.
- **Statistics:** 18 claims carry them, 26 entries in all: p-values, plus 95% bootstrap confidence intervals for the regression slopes.
- **Criteria:** all 31 claims have one.
- **Claims of absence:** two, the V4 modulation strength held across spacings (p = 0.44) and the V1 decoder generalizing to the other condition (p = 0.20). Both are judged on the paper's own test.

**Details the paper leaves open, with the readings named**
- **Neuron selection ("≥1 s.d. above spontaneous"):** compared on the mean response to the isolated targets, or on the best target.
- **Decoding:** the number of cross-validation folds (10-fold used, 5 as a variant). For Fig 2D/E, the animal (the one with 84 cases) and the unnamed test (paired t or Wilcoxon).
- **Threshold-elevation model:**
  - the binomial trial count (held-out test trials or all trials);
  - the form of the chance adjustment;
  - how the permutation test works (labels swapped within each data point is the reading used).
- **Pseudo-populations and shuffled decoding:** what "similar" means (within 2 bootstrap SEM is the reading), the population sizes, and whether shuffling applies to training trials only or to both training and test.
- **Noise correlations:** whether both stimulus epochs of a trial are used or only the first.
- **Fano factor:** whether the t test is on the raw or the log Fano factor.
- **Modulation index:**
  - the tail rule for significance: two-sided at 2.5% per tail, which the text's "expected false positive rate" implies, or one-sided 5%;
  - whether resampling pools within each orientation or across all;
  - whether "farther" means 2.6° only or the three larger spacings pooled;
  - for V4, whether the percentages are of all neurons or of the facilitated and suppressed neurons;
  - whether the V4 "±0.38" and "±0.48" are SDs. They cannot be SEMs over 691 neurons, so the tolerance is 10% of the mean instead.
- **Nearest against farthest t tests:** paired or two-sample.
- **Tuning model:**
  - whether the likelihood is over single trials or over mean responses;
  - whether means are over neuron-and-spacing cases or over neurons;
  - how even and odd trials are split.
  - The printed "p > 0.001" for the additive term sits in a sentence calling the difference significant. It is recorded as printed and judged as p < 0.001.
- **Fit quality:** mean, median or pooled.
- **Covariation of the two terms:** no measure is given; Pearson r, negative with |r| ≥ 0.5, is a standard threshold I chose, not the paper's.
- **Simulation:** the number of simulated trials, and which measured slopes it is compared with (all driven neurons or the fitted ones only).
- **"Near" and "far" in Fig 6:** 1.3° and 2.6°, or the two nearer and two farther spacings pooled.
- **Fig 7:** the unit of the paired t test, and which orientation pairs enter the summary.
- **Fig S6:** no threshold is given; "still driven" is read as a mean fraction of at least 0.8.

**Data the paper used that this dataset may not hold** (the author is to check): the receptive-field mapping sessions (Fig 1B), the coarse mapping at the start of each session (Fig S4), the waveform SNR (the well-isolated control), and a spontaneous or baseline rate for the neuron selection.
