# Hart, Frank, Lopes et al. (2023) from dandiset 000467

Tests the calcium imaging findings of [Hart et al. (2023)](https://doi.org/10.1016/j.cell.2023.05.025)
that can be tested on [DANDI:000467](https://dandiarchive.org/dandiset/000467/0.261004.1655), which holds
two-photon volumes of the right antennal lobe (AL) of GCaMP6s clonal raider ants: 6 ants given general
odorants, 3 ants imaged bilaterally, and 13 ants given four alarm pheromones at two concentrations.
The behaviour, transgenesis, confocal and genome data of the paper are not in it.

| Claim | Outcome |
|---|---|
| Each general odorant activates a unique combination of glomeruli, similar across ants | Not reproduced |
| 3-hexanone activates the broadest region | Reproduced |
| Responses to 4-methyl-3-hexanol are bilaterally symmetrical | Partially reproduced |
| The vehicle generates no responses | Not reproduced |
| Odors cause no fluorescence decreases | Not reproduced |
| Responses are often 1 to 2-fold and outlast the pulse | Not reproduced |
| At most a median of 6 glomeruli per pheromone | Reproduced (assumed) |
| Higher concentrations recruit a few more glomeruli | Reproduced (assumed) |
| One glomerulus (PGb) shared by the three panic pheromones | Not reproduced |
| 6MHO rarely shares glomeruli with the others | Reproduced (assumed) |
| PGb, 6G and PGa found in 13, 13 and 11 of 13 ants, PGb mid-depth | Not reproduced |
| Tuning of PGb, PGa and 6G | Partially reproduced (assumed) |
| PGb and PGa responses decline, 6G responses are slow | Partially reproduced (assumed) |
| 6G plateau of 30 s and return after 80 s in 144 s recordings | Not reproduced |
| Positions of PGa and 6G relative to PGb | Not reproduced |
| Shared panic pathway (imaging half) | Not reproduced |
| Temporal mixed models of PGb and PGa | Not reproduced (assumed) |
| Behaviour, transgenesis and pupae images (8 claims) | Blocked: data missing |
| Confocal and genome data held elsewhere (7 claims) | Blocked |

"(assumed)" marks an outcome that rests on the adopted reading of a method the paper leaves open: the
paper drew its ROIs by eye, and the counts of responding glomeruli rest on the ROI's mean value with
the Methods' trial-mean rule; the single-glomerulus outcomes rest on the identification of the focal
glomeruli and on a 15 um disc ROI. The other readings are shown in the notebooks.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000467-hart-2023-01.yaml`](../../attempts/000467-hart-2023-01.yaml).

- `general_odorants.ipynb`: the general odorant and bilateral experiments (about 6 minutes).
- `alarm_pheromones.ipynb`: the alarm pheromone experiment at each ant's higher concentration, the
  focal glomeruli and their traces (about 21 minutes).
- `concentration.ipynb`: responding glomeruli at both concentrations (about 17 minutes).
- `al_imaging.py`: streaming the plane files, peak fold change maps, ROIs and responding glomeruli,
  identification of the focal glomeruli and their traces. Other notebooks on this dandiset can import it.

The notebooks read only the volumes each analysis needs (volumes 1 to 5, 8 and 9 to 14 of each plane
for the maps; row bands of every volume for the single-glomerulus traces), about half a terabyte in all.
