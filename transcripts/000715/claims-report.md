I wrote the claims file at `claims/000715/10.1016-j.cell.2020.12.012.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems.

**Text read.** The accepted author manuscript from PubMed Central (PMC10494711), not the version of record. That covers the main text, STAR Methods, the legends of Figures 1–7 and S1–S3, and two supplements read from their PDFs: Methods S1 (atlas, neuron detection, identification accuracy) and Methods S2 (optimal coloring).

**Code read.**
- `amin-nejat/CELL_ID` at d9f5df9, the last commit before publication. It holds the identification software (detection, identification and a pretrained atlas). It does not hold the script that builds the atlas from the 10 worms or the cross-validation behind Figure 7B–C.
- `Eviatar/Optimal_Coloring` at 990c597. It holds the coloring solver, the rule for which neurons count as neighbors, the violation measure, and the NeuroPAL colors and reporter tables.
- I did not read `NeuroPAL-traces`, because no claim tested here uses it.

**Claims.** 32, all with quotes; 5 carry statistics (7 values) and all 32 have criteria.
- **11 testable on this dandiset**, which by its title holds the 10-worm atlas data:
  - positional variability differs across neurons;
  - OLLR is more than twice as variable as OLLL;
  - identification accuracy, 86% head and 94% tail (leave-one-out);
  - the ventral ganglion is lower than every tail ganglion;
  - 8 manual labels lift head accuracy above 90%;
  - labeling the most uncertain neurons first beats random order;
  - position-only accuracy, 50% head and 68% tail;
  - detection accuracy, 80%/88%, with precision and recall 90%/93%;
  - the confidence scores are calibrated.

  The other two of the 11 also need the coloring code's tables (`with_inputs`): NeuroPAL's color violations of 3.5%, and the optimal-coloring results of 1.7% and 10.5%. One claim uses ganglion labels from the code (`with_labels`).
- **21 marked `elsewhere`**, with a "Not tested on the dandiset" criterion: the NeuroPAL color map, strain phenotypes, receptor expression and connectome percentages, the pag-3 and eor-1 mutants, and the whole-brain imaging results. The whole-brain data are on Zenodo (doi:10.5281/zenodo.3906530); the receptor and mutant data are deposited nowhere the paper names.

**Details the paper leaves open, and the readings named:**
- **Positional variability (OLL claim):** standard deviation, variance, or the anterior-posterior extent of the 50% contour in the 2-D slice Figure 2 draws.
- **Variability across neurons:** the paper gives no test. I set the threshold from its own example: the largest per-neuron spread must be more than twice the smallest.
- **Identification accuracy:**
  - which neurons are identified: the hand-annotated ones, or automatic detections matched within 3 µm;
  - the starting alignment: Methods S1 starts from the identity, the code first aligns the worm's long axis and searches rotations (run as a variant);
  - colors: those stored in the dandiset, or recomputed by the Methods S1 rule;
  - averaging: the mean over worms, or all neurons pooled;
  - scoring: per neuron, or by left/right class (the footnote names only RMF as an example).
- **Most uncertain neuron:** highest entropy, or lowest top probability (the code's choice). Accuracy after labeling is counted with or without the labeled neurons.
- **Calibration:** the paper gives no measure. Two readings: a positive Spearman correlation, and a mean confidence-accuracy gap under 10 points.
- **Color violations:** Methods S2 counts the share of neighbor pairs below the margin; the code reports the mean shortfall below the margin (a variant). Head and tail pooled or separate is not said. The setting that yields the 3-reporter solution is not stated.
- **Detection settings:** shape bounds and filter thresholds are not given; the code defaults are used and recorded as a deviation.
- **Atlas fitting:** the random starting worm and the convergence tolerance are standard choices, with sensitivity reported.
- **Readers' note:** one sentence pairs GAR and MGL with "glutamatergic and cholinergic … respectively", which looks swapped. The criterion notes this.

**Missing from the text.** Tables S1–S6 (spreadsheets), Videos S1–S4 and the Figure S4 legend. This leaves out the per-neuron atlas values (Table S3), the mutant p-values (Table S5, so the pag-3 and eor-1 statistics are recorded only as the paper's significance threshold of 0.05), and the whole-brain statistics (Table S6). No testable claim needed a number that exists only in these tables.
