I wrote `claims/001750/10.1038-s41556-026-02009-4.yaml`. The quote checker reports **30 claims, 30 quotes, 15 statistical values, 0 problems**. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC13457102): main text, figure and Extended Data legends, Methods, and the Data and Code availability statements. There was no PDF, so the Fig. 4d box plot and its P value could not be read. The Supplementary Information and Source Data were not in the text. The Fig. 4d claims don't need them: they rest on the Results, the Fig. 4d legend and the Methods. The 001751 and 001752 readers went ahead on the same basis.

**Code read.** github.com/RFLiu2021/AIC_proj at commit 44cd8a6, and PatchAnaLab 1.0 (Zenodo 19995355).
- `Fig4d_plotNaCurrent.m` compares the absolute value of each cell's maximal Na+ current, in pA, with `ranksum`; it also runs `ttest2`.
- A per-cell table lists the deposited NWB file name, cell type and maximal current for 35 cells: 14 VEN and 21 PC, all from subject Mfa221206. The median absolute currents are 14.9 pA (VEN) and 29.3 pA (PC).
- Neither package contains the code that computes the maximal current from the traces.

**Claims.**
- **5 on this dataset:**
  - `na-cell-table-link` (a link check): the dataset's files match the code table, by file name, cell type and computed maximum.
  - `fig4d-sodium-current-lower`: the main finding, with counts n = 14 and 21.
  - `model-na-ratio`: the model's VEN Na+ conductance, 55 against 80 pS/µm², was "set based on" the recorded VEN-to-PC ratio of peak current, which implies a ratio of about 0.69.
  - `na-patch-capacitance`: patches of about 50 fF, or about 5 µm².
  - `model-sd-na-density`: Extended Data Fig. 7c. It uses the paper's model code (`data: elsewhere`), not this dataset.
- **25 on other data:** the paper's other main findings, from DANDI 001746/001751/001752, GEO, MetaboLights, NeuroMorpho and the code. They are adapted from the checked 001751 file, with the connectivity claims condensed to two.
- All 30 have quotes. 9 carry statistics (15 values) and 25 have criteria.

**Details the paper leaves open, with the readings named:**
- **Current or density.** The code settles this: peak current in pA. The Methods' model section also says "peak sodium current". Density is shown only as a variant.
- **How the peak is taken,** in three parts, all run:
  - Baseline: the trace as recorded (leak subtracted online), or with the 2 ms before the step subtracted, as in the code's example traces.
  - Steps: the 17 steps from −80 to 0 mV (the Methods, and the code's `nTraces`), or every step recorded (the code's example array holds 28).
  - Window: 0 to 20 ms (the code's plot) or the whole 25 ms step (the Methods).
- **Sampling rate and step onset.** The Methods say 100 kHz, but the code's VEN example is 50 kHz with onset at 40 ms, and its PC example is 100 kHz with onset at 20 ms. Both are read from each file.
- **Alpha.** The text prints no p for Fig. 4d, so p < 0.05 is used and labelled as the conventional reading.
- **The 0.69 ratio.** It is not printed, and "set based on" may allow rounding. The readings are the ratio of means and the ratio of medians.
- **The "~50 fF" capacitance.** The readings are the mean and the median. The paper gives no test that patch areas are "similar", so that part does not decide the claim.
- **Cell types.** If the dataset lacks them, they come from the code's CSV, and the claim becomes `with_labels`.

**One thing to flag.** The code table's values give a VEN-to-PC ratio of 0.51 (medians) or 0.58 (means). Both fall outside the tolerance of 0.69 ± 0.069. I wrote the claim from the paper as it stands and did not adjust the tolerance.

**Missing from the paper:** the Supplementary Information and Source Data, and the Fig. 4d P value, which is printed only inside the figure. No claim on this dataset needed them.
