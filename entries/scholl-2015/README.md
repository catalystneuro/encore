# Scholl, Pattadkal, Dilly, Priebe & Zemelman (2015) on CRCNS pvc-10

Attempts the findings of [Scholl et al. (2015)](https://doi.org/10.1016/j.neuron.2015.06.030) on
[CRCNS pvc-10](https://doi.org/10.6080/K0GT5K3V). The published data set holds the raw two-photon
movies (green and red channels), stimulus tables and plane shifts of six PV-Cre;Ai14 mice, and 50
unlabelled example cell masks for one plane. It holds no masks or PV+/PV- labels for the paper's
hand-identified cells and none of the per-cell measures its descriptor lists, and it does not
include the CaMKIIa mice, the neuropil patches or the histology. All 25 claims are blocked
(`data_missing`).

The notebook checks the files against the descriptor and the paper (planes, repeats, frame sizes,
onset intervals, duplicates), streams one plane with the example masks to check that the stimulus
table shares the movie's clock, and estimates the time to stream all 252 GB of movies.

The attempt record, with the reasons and the findings about the data set, is
[`attempts/scholl-2015-01.yaml`](../../attempts/scholl-2015-01.yaml).
