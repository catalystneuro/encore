I wrote `claims/000981/10.1016-j.cub.2026.08.040.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record (a PDF supplied by a person, extracted to text). That covers the main text, the STAR Methods, and the legends of Figures S1 to S20. I read no figure from the PDF because no page renderer was installed.

**Code read:** `venkatachalamlab/whole-brain-chemosensory-responses` at commit b0dbdbf (1 June 2025). That commit is tag 1.0.0, which is the Zenodo record the paper cites. Its `datasets.json` lists 22 hermaphrodites and 25 males, which matches the paper and the 47 assets of the dandiset.

**Counts:**
- 32 claims; all 32 have quotes, none use `inferred`.
- 4 have statistics, all p < 0.05 t-tests for dimorphism examples.
- 32 have criteria and 6 have expected values. Expected values are the class counts 84 and 80, the per-layer counts, R² = 0.8, the SEM figures 1.14/2.07 → 0.62/0.87, and the animal counts 22 and 25.
- 5 claims need outside connectome data (`with_inputs`): Fig 4D, 4F, 4G, S20 and the normalization numbers.

**Details left open, with the readings named:**
- **Which presentations are excluded:** (a) the Methods' 5×IQR outlier rule alone; (b) that rule plus the code's extra filters: an artifact rule on trace ranges, identification confidence 1 only, more than 7 missing frames, and per-recording time ranges and ganglia to ignore.
- **Which layer each class belongs to:** the 24/36/15/14 split is only in Figure 5A, Data S4 and the code's missing `neuron_classes.json`. The author must use an assignment with these totals, list it, and record it as a deviation.
- **Whether a class counts as dimorphic only when it is also responsive:** (a) yes, as the code does; (b) dimorphic alone.
- **How functional connectivity is averaged and tested:** (a) the code's way, pooling L/R combinations across animals, removing values beyond 3 IQR, and testing the pooled values; (b) the Methods' way, a per-animal mean first.
- **Synaptic regularization:** 5 in the Methods; the code's 3 is a variant. The cut-off for top functional pairs is p < 0.01 in the Methods; the code's p < 0.001 is a variant.
- **Motor state from AVA:** which AVA trace (AVAL, AVAR or their mean), how the "20% change" is measured (range/mean or last vs first), and whether the bleaching fit is subtracted or divided. All combinations are run. Counting state-dependent pairs uses q < 0.05 or p < 0.05.
- **Onset or offset window** where the text doesn't say (BAG, I2, ADF/M2), and **which salt** for I2.
- **Vague words in the paper:**
  - "almost all": at least 95% or at least 99% of pairs.
  - "largely unaffected" (S3E): robust in all three representations, or in each of the other two separately.
  - "nearly every": at least 90%, from the paper's own use of it.
  - "predominantly": most of the tests.
- **Stimulus order (S2E):** no test is named, so three are run: regression on all neuron responses, regression on per-animal means, and a one-way ANOVA.
- **Which traces for the left/right similarity (S2F):** band-passed or raw.
- **Correlation summaries (stimulus–layer, pharynx):** mean |r| or RMS r.

**Missing from the paper and code:**
- **Paper supplement:** Data S1–S4 are not in the text. Data S4 is what fixes the layer assignment.
- **Files the code reads but the repository doesn't hold:** `neuron_classes.json`, the metadata spreadsheet, `confidence.csv`, the stimulus-order files, and the connectome table prepared by S.J. Cook.
- **Analyses added at revision:** the code predates the revision. It has nothing for the cycle-1 and per-animal tests, the FDR correction, the AVA motor-state analyses, or Figures S2E and S2F; those claims rest on the Methods alone.
- **Wrong figure citation:** the text cites Figure S2C for the male-specific neurons, but the legend that shows them is S2D.
- **Behavior claim:** the drop-test data probably aren't in the dandiset, and Figure 1C's per-stimulus preferences can't be read from the text.
