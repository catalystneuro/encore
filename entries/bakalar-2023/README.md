# Bakalar et al. (2023) from dandiset 001362

Tests the findings of [Bakalar et al. (2023)](https://doi.org/10.1111/jne.13286) that can be tested
on [DANDI:001362](https://dandiarchive.org/dandiset/001362/0.260923.2152), which holds the
whole-brain c-Fos light-sheet experiment of the paper (Figure 5, Table 4): for 22 hemispheres of 6
PACAP fl/fl and 7 PACAPko mice, the corrected stacks, the registered atlas labels and the CATNIP
derivatives. The behaviour, qPCR, section immunohistochemistry, in situ hybridization, body weight
and telemetry data of the paper are not in it.

| Claim | Outcome |
|---|---|
| DG-sg and DG-po have more c-Fos cells in PACAPko (Figure 5) | Blocked: methods underspecified |
| 13 more regions at raw p <= 0.01, including SNr, STN and IGL (Table 4) | Blocked: depends on the claim above |
| U and percentages of the 15 regions of Table 4 | Blocked: depends on the claim above |
| 24 claims on behaviour, qPCR, sections, in situ hybridization, weight and telemetry | Blocked: data missing |

The c-Fos claims were run: cells were recounted from the deposited segmentations by the rule of the
Supplemental Methods, under every reading of the details the paper leaves open (the FRST threshold,
the region size, the outlier rule). DG-sg and DG-po are higher in PACAPko under every reading. Both
are significant after correction in 12 of the 20 readings at thresholds 4000 to 12000, and in none
of 56 analyses at 14000 to 26000 (18 hemispheres). As the readings disagree, the claims file blocks
the claim. Thresholds 28000 to 40000 were not run, for time. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/bakalar-2023-01.yaml`](../../attempts/bakalar-2023-01.yaml).

- `reproduce_bakalar_2023.ipynb`: the analysis. It took 66 minutes in the last run, over the
  60-minute limit, most of it streaming and counting the segmentations.
- `reproduce_bakalar_2023_thresholds_14000_26000.ipynb`: the same tests at thresholds 14000 to 26000
  on the 18 hemispheres that hold them (35 minutes).
- `fos.py`: loading the files, the recount of cells per atlas region, the region exclusions and the
  region-wise tests. Other notebooks on this dandiset can import it.
