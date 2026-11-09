I wrote `claims/000008/10.1038-s41586-020-2907-3.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems. Nothing is committed.

**Text read.** The version of record (open access) from Europe PMC (PMC8113357): main text, Methods, figure legends and Extended Data legends. There was no PDF, so the Extended Data figures were read from their legends only. Not in the text: Extended Data Tables 1–2 (t-type descriptions) and Supplementary Files 1–3 (galleries, dot plots, the list of morphometric statistics). No claim rests on numbers that appear only in those, so I did not stop.

**Code read.** github.com/berenslab/mini-atlas at commit `3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9`. Besides the notebooks, it holds the paper's per-cell metadata, the feature tables and the count tables. Where the Methods are silent and the code decides, the criteria follow the code and cite it.

**Claims: 32.**
- **Quotes:** all 32 have one; none needed `inferred`.
- **Statistics:** none. The text reports no p-value or interval for any finding. The r values it does give (0.60, 0.70) are recorded under `expected`.
- **Criteria:** 31 of 32. The one without (`rnaseq-depth`) is judged on its expected values alone. 15 claims have expected values.
- **Data:** 16 `dataset`, 11 `with_inputs`, 5 `elsewhere`.
  - `dataset`: cohort, ages, genotypes, stimulus protocol, the Extended Data Fig. 4 example cell, feature counts, family features, kNN family separation, the IT/ET features, the t-type and depth claims, and the Fig. 5 variability claims.
  - `with_inputs`: reduced-rank regression, the Fig. 4 distance correlations, the t-SNE overlay claims, morphology combined with electrophysiology, and hold time against cDNA yield.
  - `elsewhere`: sequencing (GEO GSE163764 / NeMO) and morphology (Brain Image Library).
- **t-type labels:** claims that need a cell's t-type are marked `dataset`. Whether the NWB files carry it is left for the author to find, and the opening comment says so.

**Details the paper leaves open, with the readings named:**
- **Cell count:** 1,329 cells, or 1,328 if the one cell whose recording failed quality control is missing.
- **Age statistics:** taken over mice or over cells.
- **Stimulus interval:** measured onset to onset or offset to onset; "most" cells repeated means more than half.
- **Example cell (Extended Data Fig. 4):**
  - The legend does not name it; the code does (20181112_sample_11).
  - Its AP threshold is −40.18 mV in the legend but −43.18 mV in the code's table. Both readings are reported.
  - The legend prints the sag time as "0.26 ms"; the table has 0.26 s.
- **"High" firing, sag and rebound:** compared with all seven families, or with the four interneuron families.
- **Fig. 4c:** the code leaves out Sst Chodl and Pvalb Vipr2_2; the Methods don't say. Both readings are run, and the reported 50 t-types and 200 pairs show which one the paper used.
- **Extended Data Fig. 7:** "multiple families" means at least two, or a majority.
- **Fig. 4a, 5c, 5d (colour overlays only):** two readings each, one from embedding positions and one from transcriptomic distance. If they disagree, the claim is blocked as `methods_underspecified`.
- **Fig. 4b:** all 17 features (the code's Extended Data Fig. 6i analysis), or rebound alone.
- **Fig. 5a:** "Vip Mybpc1" means any one of its t-types, or all of them pooled.
- **Fig. 5b:** "many" means at least a quarter, or at least a third, of the t-types.
- **Reduced-rank regression:**
  - The penalty λ is 0.5 in the Methods and 0.45 in the code's cross-validation; both are run.
  - The Methods log-transform four features; the code's regression notebook does three. The Methods' choice is the main reading and the code's a variant.
- **Mismatched cells:** the Methods name 4 RNA/phenotype mismatches plus 1 cell outside MOp. The code's table lists 6 plus 1. Both counts are reported.
- **No measure at all:**
  - Fig. 4e (Pvalb axon shape) is recorded for coverage only.
  - Where the paper gives no test (Fig. 1b, the L4/5 IT_1 layer boundary, Extended Data Fig. 8 Leiden entropies), I fixed thresholds from the paper's own layer boundaries and its 25% misclassification cut, and the criteria say so.

**Missing from the paper:** the cut-off for "strong overlap" in Fig. 3d is not stated; the Fig. 5a legend's 25% was used. The p-value in Extended Data Fig. 6i appears only in the figure. No claim lacked text it needed beyond these.
