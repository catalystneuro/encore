I wrote `claims/001605/10.1038-nn.4390.yaml`: 39 claims, every one with a word-for-word quote. Nothing is committed. The quote checker passes every quote. It still lists five supplement p-values as not found, because the supplement prints "×" as an unreadable glyph; I read each of them in the text (1.27e-4, 9.81e-8, 4.26e-5, 2.15e-7, 8.60e-4).

**Text read:** the version of record (Nature Neuroscience, December 2016), with the Online Methods and the supplement (Supplementary Figs. 1 to 14 and Table 1). Nothing the results rest on is missing. I rendered PDF pages only to read Figs. 1c, 2c,d and 4, and the columns of Supplementary Table 1. The paper links no code (Matlab "available from corresponding author upon request"), so I read none.

**Counts:**
- 39 claims, all with quotes and criteria.
- 35 carry statistics, about 76 test entries in all.
- 7 carry expected values: session and mouse counts, neuron counts, behaviour timing, licking correlation range, sound-responsive percentages, neuron-class counts and task-relevant percentages.
- Every claim uses the dataset's own data (`data: dataset`); the paper uses no outside data.
- Six claims are muscimol and sound-mapping experiments. The archive description lists only the 94 imaging sessions, so the author must check whether these are in the dataset.

**Details the paper leaves open, with the readings named (O1 to O9 in the opening comment, plus some per claim):**
- **O1, baseline of the task-relevance t-test:** (a) zero, the session mean the signal is taken against; (b) the neuron's mean during inter-trial intervals.
- **O2, alignment windows:** read from the Fig. 2c axes. The start-aligned distance window is given nowhere: (a) 0 to 67 cm; (b) 0 to 33 cm.
- **O3, k-means feature splitting after-reaching from reward neurons:** (a) the normalized 16-frame trace before the goal; (b) its mean.
- **O4, distance preference:** the peak of the distance-aligned trace (one reading, from Fig. 2d).
- **O5, percentages:** (a) mean of per-session proportions; (b) pooled counts.
- **O6, single-neuron regression:** frames run (a) from start to goal or (b) to 3 s after it. The four initial width values are not given; two sets are named.
- **O7, positive shift before the log-normal likelihood:** the minimum set to (a) 0.01 or (b) 0.1.
- **O8, Fig. 4 bins:** 4.2 cm (tick spacing and decoder bin), or 0.42 cm. The Fig. 5 zones come from the axes.
- **O9, slow/fast split:** by (a) whole-trial or (b) zone speed. Zones analysed: (a) all no-sound zones or (b) the one nearest the goal.
- **Per claim:**
  - Fig. 1c: bin width and which bins are compared.
  - Licking correlation: Pearson or Spearman.
  - Tuning similarity: which fitted coefficient, the width s or b1.
  - Sound-intensity model: silent zones and the cap below 25 cm.
  - Chance level for decoding: flat prior, or labels permuted across trials.
  - Supp. Fig. 9: the four group borders.
  - Log-normal vs Gaussian: the measure of "better".
  - SVM: kernel, classes and error measure.
  - Behaviour timing: which no-sound zones count.

**Inconsistencies noted:**
- The text says "25.8 cm" where the figures use 25.1 cm.
- The Fig. 4c legend calls RMSE an "expected squared deviation", without the root.
- Supplementary Fig. 8c's p-value pairs only support the text when read in the order intermittent 1, then intermittent 2. I recorded that reading in the criterion.

Nothing a claim needed is missing from the paper beyond these open details. The figure pages could not be opened with the PDF reader because poppler isn't installed. I installed PyMuPDF into the temporary directory to render them; nothing in the repository changed.
