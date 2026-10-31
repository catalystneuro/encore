# Hart, Lopes, Frank & Kronauer (2024) from dandiset 000773

Tests the findings of [Hart et al. (2024)](https://doi.org/10.1016/j.cub.2024.05.031) on
[DANDI:000773](https://dandiarchive.org/dandiset/000773/0.261004.1511), which holds the two-photon
calcium imaging of the right antennal lobe of 21 GCaMP6s clonal raider ants (14 at 48% and 7 at 3%
odor concentration), young (15 to 20 days) and old (60 to 61 days), each with two alarm pheromones
and five general odorants three times and a paraffin oil control, 33 planes per trial.

| Claim | Outcome |
|---|---|
| Behaviour (Figure 1, S1, Table S1), five claims, on the paper's Data S1 | Reproduced |
| Total GCaMP6s fluorescence does not change with age (Figure 2B) | Blocked: the Brain Image Library could not be reached |
| Whole-AL alarm pheromone response does not change with age (Figure 2D) | Reproduced |
| Whole-AL 3-hexanone and isopropanol responses fall with age (Figure S3B) | Partially reproduced (the fold ratios are not reached) |
| No whole-AL age effect for the other odorants and concentrations (Figure S3B) | Reproduced |
| Fewer glomeruli respond to 4-methyl-3-heptanone in old ants (Figure 2E) | Blocked: methods underspecified |
| Alarm pheromones are represented sparsely | Blocked: methods underspecified |
| No age effect on response breadth for three general odorants (Figure S3C) | Blocked: methods underspecified |
| Link: the focal glomeruli can be found from Data S2 | Partially reproduced |
| Mean of the six focal glomeruli does not change with age (Figure S2A) | Reproduced |
| G2 response to 4-methyl-3-heptanone falls with age (Figure 3B) | Not reproduced |
| PGb and PGa responses to alarm pheromones rise with age (Figure 3D) | Not reproduced |
| PGb and PGa responses do not differ between 60 and 90 days (Figure 3D) | Blocked: methods underspecified |
| Which focal glomeruli general odorants excite (Figure S4A) | Not reproduced |
| 3-hexanone and isopropanol responses fall in five of six glomeruli (Figure 4) | Partially reproduced |
| Small propionic acid deflection in G2 and G3 declines with age (Figure 4) | Not reproduced |
| PGb 3-hexanone response is lower but slower in old ants (Figure S4D) | Partially reproduced |
| PGb and PGa are modulated in opposite directions for pheromones and odorants | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds no ROI positions, so the six focal glomeruli, drawn by hand in the paper, are
placed here where the dandiset's per-trial responses follow the paper's per-glomerulus traces in
Data S2. Every young-ant placement is above chance, but 15 of 39 old-ant placements are not. The
focal glomerulus claims are measured where each glomerulus was placed without the trials being
tested (leave one odor out), so that the tested values did not choose the place; on those held-out
trials only 9 of 52 old-ant glomerulus traces follow Data S2's. The claims that rest on old ants'
alarm responses fail, and PGb's alarm AUCs measured from the imaging are well below Data S2's
Figure 3C and 3D values in both this dandiset and DANDI 000467. Run on Data S2's own values, every
focal glomerulus claim holds as the paper states it.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000773-hart-2024-01.yaml`](../../attempts/000773-hart-2024-01.yaml).

- `reproduce_hart_2024.ipynb`: the analysis. It streams about 460 GB by HTTP range requests (only
  the frames needed), including the eight 90-day ants of DANDI 000467, and takes about 30 minutes.
- `antal.py`: listing and streaming the files, the peak fold change maps of the Methods, the AL
  outline, responding ROIs, locating the focal glomeruli and reading their traces, and the
  behaviour fits. Other notebooks on this dandiset can import it.
