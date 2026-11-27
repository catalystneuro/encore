# Costabile, Balakrishnan, Schwinn & Haesemeyer (2023) from dandisets 000235 to 000238

Tests the zebrafish findings of [Costabile et al. (2023)](https://doi.org/10.7554/eLife.83289)
on the four dandisets the paper deposited: [000235](https://dandiarchive.org/dandiset/000235/0.230316.1600)
(forebrain), [000236](https://dandiarchive.org/dandiset/000236/0.230316.2031) (midbrain),
[000237](https://dandiarchive.org/dandiset/000237/0.230316.1655) (hindbrain), 25 larval zebrafish
imaged during a random-wave heat stimulus, and [000238](https://dandiarchive.org/dandiset/000238/0.230316.1519),
six fish with reticulospinal backfills.

| Claim | Outcome |
|---|---|
| 25 fish, 750 planes, 706,543 components, 432,882 pass the brightness criterion | Reproduced |
| Training and test data are largely uncorrelated | Reproduced (rests on an assumption) |
| Claims on the MINE fits of the zebrafish neurons (18, including six that also need the Z-Brain registration) | Blocked: too large |
| Reticulospinal neurons are mostly behavior-driven | Blocked: no backfill annotation in 000238 |
| Simulations (Figures 1 to 4) and mouse widefield data (Figure 5), data elsewhere (14) | Blocked: not attempted in this run |

The files hold the paper's counts of fish, planes and components exactly, and the clock checks are consistent with one clock. Most of the paper's
analyses rest on a CNN fit to each of about 433,000 neurons; on this runner that takes many times
the five hours of a run (the hours are printed in `mine_fits_subsample.ipynb`, twice as many with
the rotated controls), so those claims are blocked. The paper's linear comparison model, fit here to every
neuron, identifies about 26,300, close to the roughly 25,300 the paper implies, and a random subsample of
600 CNN fits gives estimates consistent with the paper's Figure 6D, with wide intervals
(`mine_fits_subsample.ipynb`). In 10 planes the tail timestamps jump once by 128 s; the time ranges show which side is misplaced. The dandisets hold no swim bouts, no Z-Brain registration and
no annotation of the backfilled neurons; the bouts are re-derived here from the tail tracking.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/costabile-2023-01.yaml`](../../attempts/costabile-2023-01.yaml).
