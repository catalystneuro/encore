# Chen, He et al. (2026) from dandiset 001933

Tests the findings of [Chen, He et al. (2026)](https://doi.org/10.1038/s41467-026-75194-3) on
[DANDI:001933](https://dandiarchive.org/dandiset/001933/0.260825.1457), version 0.260825.1457, which holds the fiber
photometry of Figure 6 and Supplementary Figures 7 and 8: GRAB-DA3m in the dorsal striatum during optogenetic
stimulation of Anxa1+ (15 mice) or Calb1+ (12 mice) SNc dopamine neurons, in LRRK2-WT and LRRK2-G2019S mice. The
imaging, proteomics and western blots of Figures 1 to 5 are not in the dandiset. The paper deposited them on Zenodo,
in PRIDE and in the BioImage Archive, and their claims are tested on those data and counted apart.

The current attempt, [`attempts/001933-chen-2026-02.yaml`](../../attempts/001933-chen-2026-02.yaml), applies protocol
pilot-7 to the same version as the first attempt,
[`attempts/001933-chen-2026-01.yaml`](../../attempts/001933-chen-2026-01.yaml). The photometry results are unchanged;
the claims of Figures 1 to 5, blocked in the first attempt, are now tested.

| Claim | Outcome |
|---|---|
| The paper's source data can be recomputed from the dandiset | Not reproduced (Anxa1 links; Calb1 does not) |
| Anxa1 evoked release lower in G2019S at 0.5 mW | Reproduced |
| 7 of 8 Anxa1 G2019S mice reduced, 3743 not | Reproduced |
| Anxa1 reduction at all four powers | Reproduced |
| Anxa1 spontaneous transients smaller in G2019S | Reproduced |
| 6 of 8 Anxa1 G2019S mice with smaller transients | Partially reproduced |
| Calb1 spontaneous transients not reduced | Reproduced (p = 0.051, at the threshold; 0.040 to 0.079 as the window moves) |
| Calb1 evoked release reduced at four powers | Reproduced |
| Only 2 of 7 Calb1 G2019S mice reduced | Partially reproduced |
| Cohen's d larger for Anxa1 (2.05) than Calb1 (0.76) | Not reproduced |

On the data in other archives, counted apart: LRRK2 higher in Aldh1a1+ neurons, p-RAB3A and p-RAB3C raised in G2019S,
RIM1 lower in synaptosomes and no TH fibre loss are reproduced; RIM1/2 and RILPL1/2 binding (three of four
comparisons, as RILPL2 is found only in the p-RAB3A pulldowns), fewer bassoon+ synaptosomes and the bassoon changes
in vulnerable axons are partially reproduced; and the phosphoproteomics claim
(289 peptides, including RAB3 T86) is not reproduced, as in the deposited data the RAB3 T86 phosphopeptide is higher in
the samples labelled MLi-2.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences
from the paper's method.

The Anxa1 recordings are those behind the paper's figures: its published traces equal the dandiset's dF/F. The Calb1
dF/F in the dandiset is not the one behind Supplementary Figure 8, so the Calb1 results here are of the dandiset's
processing. The attempt record gives the reasons and the differences from the paper's method.

- `reproduce_chen_2026.ipynb`: the analysis. It takes about ten minutes, most of it streaming the NWB files and
  the 168 synaptosome images.
- `lrrk2.py`: loading the files, the evoked and spontaneous measures of the paper's Methods and code, the dF/F
  recomputed from the raw signal, and the paper's source data. Other notebooks on this dandiset can import it.
- `archives.py`: reading the paper's Zenodo, PRIDE and BioImage Archive deposits, the statistics of the Figure 1 to 5
  legends, and a re-implementation of the Methods' FIJI analysis of synaptosome images.
