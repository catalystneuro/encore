# Ishii et al. (2025) from dandiset 001249 and its Figshare deposit

Tests the findings of [Ishii et al. (2025)](https://doi.org/10.7554/elife.91765) on
[DANDI:001249](https://dandiarchive.org/dandiset/001249/0.241109.2357), which holds the whole-brain
light-sheet volumes of the 14 brains behind Figure 2, and on the authors' Figshare deposit
([doi:10.6084/m9.figshare.27642768.v1](https://doi.org/10.6084/m9.figshare.27642768.v1)), which
holds the data of every other figure.

| Claim | Outcome |
|---|---|
| Figure 2, whole-brain TRAP densities (seven claims, the only ones on the dandiset) | Blocked: too large |
| Figure 1 and its supplements, mating behavior after ejaculation (six claims) | Reproduced |
| Figure 3, HCR: Fos in the MPN, in Vgat and Vglut2 cells and in marker subsets (three claims) | Reproduced |
| Figures 4 and 5, response magnitudes, responders, specific classes (four claims) | Reproduced |
| Figure 6C, Vgat ejaculation responders decay more slowly | Reproduced, resting on an assumption |
| Figure 6K, the late response cluster holds only Vgat cells | Reproduced |
| Figure 7F and G, only post-ejaculatory ensemble activation suppresses motivation | Partially reproduced |
| Figure 7 and its supplements, other chemogenetic results (four claims) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds only raw volumes, with no registration, segmentation or cell counts, so the
Figure 2 claims would need 1.38 TB streamed, registered to an atlas and segmented with a classifier
that is not deposited. The decay length of Figure 6C is reproduced
under the reading from the peak that a reader added to the claims file, which matches the deposited
values, provided cells that never return below 0 count as 120 s, as the deposited table has them;
the readings from onset do not reproduce it. Figure 7F and G hold by the code's signed-rank test but not fully by the
rank-sum test the legend names; whether the claims file should take the signed-rank test as its main reading is asked of a reader. The results of Figures 4 to 6 treat cells as units, as the paper does; with animals as units the magnitude differences of Figure 4H and the decay length of Figure 6C are not significant. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/001249-ishii-2025-01.yaml`](../../attempts/001249-ishii-2025-01.yaml).

- `reproduce_ishii_2025.ipynb`: the analysis. It takes a few minutes, most of it streaming.
- `mpoa.py`: reading the dandiset and the Figshare zips in place, the statistics as the paper's
  code runs them, and the calcium imaging measures (magnitude, decay length, spectral clustering).
