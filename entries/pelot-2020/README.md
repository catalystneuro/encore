# Pelot et al. (2020): vagus nerve morphology of human, pig and rat

Tests the claims of Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell and Grill (2020),
"Quantified Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat",
Front. Neurosci. 14:601479, on seven SPARC datasets: the rat traces (SPARC 60, version 5), pig MT
traces (64, version 4), human anti-claudin-1 traces (65, version 8), pig anti-fibronectin traces
(89, version 1), and the MT micrographs of rat (16, version 5), human (61, version 3) and pig (82,
version 1). Everything is streamed from the public SPARC bucket at pinned object versions.

- `reproduce_pelot_2020.ipynb`: data check, one section per claim, summary.
- `pelot.py`: reading the datasets, morphometry as the paper's deposited MATLAB code does, and the
  readings made by eye for the three claims judged on micrographs.
- `mixed.py`: REML mixed models, type III F tests with Kenward-Roger (and, as a variant,
  Satterthwaite) degrees of freedom, and Tukey's HSD on least squares means.

Of 43 claims, 37 are reproduced, 3 partially reproduced and 3 not reproduced. The literature
values of Figure 7 (Supplement 4, not supplied) are read from the paper's plotting code deposited
in the datasets. A failure to reproduce here may be a failure
of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

Run with `python tools/entry.py all entries/pelot-2020`; about 8 minutes, 1.3 GB of memory.
