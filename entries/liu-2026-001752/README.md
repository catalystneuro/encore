# Liu, Huang, Shen, Shao, Jing et al. (2026) from dandiset 001752

Tests the findings of [Liu et al. (2026)](https://doi.org/10.1038/s41556-026-02009-4) on
[DANDI:001752](https://dandiarchive.org/dandiset/001752/0.260825.0222), which holds 84 voltage-clamp
recordings of spontaneous and miniature EPSCs and IPSCs from von Economo neurons (VENs) and pyramidal
cells (PCs) of the macaque anterior insular cortex (Fig. 5a-c). The files carry no cell type; it is taken
from the table of deposited files in the paper's code, and a link claim checks that table.

| Claim | Outcome |
|---|---|
| The code's table links the files to their cell types | Partially reproduced |
| sEPSC frequency lower in VENs | Blocked: the two threshold readings disagree |
| sIPSC frequency lower in VENs | Blocked: the detection measures noise in these files |
| mEPSC frequency lower in VENs | Not reproduced |
| mIPSC frequency lower in VENs | Blocked: the two threshold readings disagree |
| sEPSC, mEPSC and mIPSC amplitudes do not differ | Reproduced (three claims) |
| sIPSC amplitudes do not differ | Blocked: the detection measures noise in these files |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The paper detected events in miniAnalysis with settings it does not give beyond a 5 pA threshold. A
check of the detector (peaks of the opposite polarity as a noise null, and synthetic events injected into
every trace) shows that at 5 pA it is reliable in the files with noise below 2 pA (all mEPSC, most mIPSC,
about half the sEPSC files). In the noisier files a large part of what it counts is noise: in the sEPSC
files with noise of 2 to 4 pA it finds opposite-polarity peaks at about half the rate of the events, and in
13 of the 15 sIPSC files at about the same rate or more (about half in the other two). The threshold at each
recording's RMS noise counts noise everywhere. For this reason the two sIPSC claims are blocked
(methods_underspecified), as the third verification round agreed. The mEPSC labels of the code's file table
are the opposite of its analysis sheet's, and the sheet's own values give the paper's result only with the
sheet's labels. The frequency outcomes should be read with the notes in the attempt record.

A second notebook, `elsewhere_liu_2026.ipynb`, tests claims whose data are elsewhere, on the code's
per-cell tables, on DANDI:001750 (Na+ currents), on DANDI:001746 (Patch-seq electrophysiology), on the
metadata of DANDI:001751 (multi-patch) and on MetaboLights MTBLS13927; they are counted apart from the
dataset. The claims on the scRNA-seq atlas and the NEURON model are blocked. The AP width and amplitude
test of Fig. 4a-c is not reproduced on the Patch-seq cells of DANDI:001746, which may not be the cells
of the figure.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/liu-2026-04.yaml`](../../attempts/liu-2026-04.yaml).
