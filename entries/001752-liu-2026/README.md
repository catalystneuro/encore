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
| sIPSC frequency lower in VENs | Not reproduced |
| mEPSC frequency lower in VENs | Not reproduced |
| mIPSC frequency lower in VENs | Blocked: the two threshold readings disagree |
| sEPSC, sIPSC, mEPSC and mIPSC amplitudes do not differ | Reproduced (four claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The paper detected events in miniAnalysis with settings it does not give beyond a 5 pA threshold. The
detector used here finds 4.6 to 15 times the events of the code's per-cell sheets in the noisier sEPSC
and sIPSC recordings, and the mEPSC labels of the code's file table are the opposite of its analysis
sheet's, so the frequency outcomes should be read with the notes in the attempt record.

A second notebook, `elsewhere_liu_2026.ipynb`, tests claims whose data are elsewhere, on the code's
per-cell tables, on DANDI:001750 (Na+ currents) and on DANDI:001746 (Patch-seq electrophysiology); they
are counted apart from the dataset. The claims on the scRNA-seq atlas and the NEURON model are blocked.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001752-liu-2026-01.yaml`](../../attempts/001752-liu-2026-01.yaml).
