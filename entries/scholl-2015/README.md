# Scholl, Pattadkal, Dilly, Priebe & Zemelman (2015) on CRCNS pvc-10

Attempts the findings of [Scholl et al. (2015)](https://doi.org/10.1016/j.neuron.2015.06.030) on
[CRCNS pvc-10](https://doi.org/10.6080/K0GT5K3V). The published folder of the data set (`live/`)
holds the raw two-photon movies, stimulus tables and plane shifts of six PV-Cre;Ai14 mice and 50
unlabelled example masks, and none of the per-cell data its descriptor lists. Processed per-cell
structs for mice 7 to 10 sit in an undocumented folder of the same bucket,
`original/to_remove/`; their stored traces equal the mask means of the published movies. This
attempt uses them, for mice 8 to 10 (and the PV+ cells of mouse 7), taking the cells in the
authors' `binocmonocinds` lists as the visually responsive cells.

Of 25 claims, 7 are blocked (`data_missing`: histology, CaMKIIa mice, neuropil patches, counts of
all identified cells), 6 reproduced, 4 partially reproduced and 8 not reproduced. Most outcomes
rest on the choice of cell set and are marked as assumed; the notebook shows every reading. The
counts of cells are about half the paper's, from 3 of its 6 animals.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The attempt record, with the reasons and the findings about the data set, is
[`attempts/scholl-2015-01.yaml`](../../attempts/scholl-2015-01.yaml).
