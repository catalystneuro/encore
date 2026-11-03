# Fujimoto, Fujimoto, Elorette et al. (2026) from dandiset 001785

Tests the findings of [Fujimoto et al. (2026)](https://doi.org/10.1038/s41593-026-02301-4) on
[DANDI:001785](https://dandiarchive.org/dandiset/001785/0.260615.1835), which holds the FA maps and
normalized seed connectivity maps of the stimulated monkeys N and T, the implanted control D and the
nonsurgical controls B, W and H, with CC1 and DAPI immunofluorescence images and electron
micrographs of the cingulum bundle.

| Claim | Outcome |
|---|---|
| The seed maps, the FA maps and the cell counts can be linked to the paper's source data | Reproduced, reproduced, partially reproduced |
| Movement and foraging increase after DBS (data in DANDI:001773) | Reproduced |
| No behaviour change in the implanted control | Not reproduced (foraging falls) |
| FA rises in the stimulated CB, mid-cingulate part only, in both animals; no other tract changes | Reproduced (four claims) |
| More CC1-positive oligodendrocytes in the stimulated MCC-CB, DAPI unchanged | Reproduced (two claims) |
| No oligodendrocyte change in the dACC-CB | Not reproduced |
| No oligodendrocyte change in the UF-FM overlap | Reproduced |
| No oligodendrocyte change in the implanted control | Blocked: the size filter, which the paper does not give, decides the outcome |
| Lower g-ratio in the stimulated MCC-CB | Blocked: hand measurements not in the dandiset |
| Seed connectivity of the SCC: before DBS, decreases, increases, both monkeys, both hemispheres, networks, no motor or visual change, SAN | Reproduced (ten claims) |
| FA and connectivity in the implanted control | Reproduced (four claims) |
| Whole-brain connectivity matrices (five claims) and the control group's voxel map | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no tract or ROI masks. Which voxel belongs to which tract, CB subregion or target
ROI is taken from the paper's source data in DANDI:001773, so the FA and seed results repeat the
paper's statistics on the dandiset's values. Cells are counted here from the images, by an
automatic approximation of the paper's FIJI counts that matches them in three of the four regions. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/001785-fujimoto-2026-01.yaml`](../../attempts/001785-fujimoto-2026-01.yaml).

- `reproduce_fujimoto_2026.ipynb`: the analysis. It takes about six minutes, most of it streaming
  the 360 immunofluorescence images.
- `fujimoto2026.py`: streaming the NIfTI and TIFF files, linking them to the source data, MATLAB's
  anovan (type III) and multcompare (Tukey-Kramer on marginal means), and the cell counts. Other
  notebooks on this dandiset can import it.
