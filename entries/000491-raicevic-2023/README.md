# Raicevic, Forer, Ladrón-de-Guevara, Du, Nedergaard, Kelley & Boster (2023) from dandiset 000491

Tests the findings of [Raicevic et al. (2023)](https://doi.org/10.21203/rs.3.rs-2587250/v1) on
[DANDI:000491](https://dandiarchive.org/dandiset/000491/0.230602.1307), which holds the 3D
two-photon stacks and the final vessel and PVS segmentations of 14 pial artery segments in 9 mice.
Starting from the deposited segmentations, the notebook takes cross sections normal to the vessel,
measures the PVS and vessel areas, fits the vessel circle and the ellipse, spline and polynomial
shapes, and computes the hydraulic resistance per unit length. Every reading of the claims file's
open method details is run, and the tables show each, except reading (b) of P2 (all skeleton
points), which is run for the cross-section counts only.

| Claim | Outcome |
|---|---|
| 54 to 451 cross sections per segment, 0.8 um apart | Not reproduced (change to reproduced proposed) |
| 2D and 3D segmentations overlap by at least 70% | Blocked: data missing |
| PVS area on vessel area, slope 1.05, R2 0.158 | Not reproduced |
| Area ratio peak 1.12, median 1.88, IQR 1.79 | Not reproduced |
| PVS area varies more between segments than within | Blocked: methods underspecified |
| Per-location area ratio peaks 0.6 to 11.43, 13 locations within 30% | Not reproduced |
| Polynomial fit closest in area ratio (73, 19, 8%) | Reproduced (4 of 96 combinations) |
| Fit area ratio peaks and medians (Table 2) | Partially reproduced |
| Resistance power law in area, exponent -1.75, R2 0.944 | Partially reproduced |
| Segmentation resistance peak 1.73e15, median 3.84e15 | Not reproduced |
| Per-location resistance peaks and share within 37% | Not reproduced |
| Polynomial fit closest in resistance; fit peaks | Partially reproduced |
| Ellipse and annulus similar, both underestimate | Reproduced (one combination) |
| Spline resistance peak about 5 times the segmentation's | Reproduced |
| Velocities: ellipse faster, spline slower, polynomial closest | Reproduced |
| Vessel radius peak 28 um | Reproduced |
| Ellipse parameters (R3, R3/R1, R2/R1, R3/R2, Ov, Oh) | Not reproduced |
| HC peaks at zero; connecting channel below 0.5 R1 | Reproduced |
| Widths WS/R1, WL/R1, WS/WL | Not reproduced |
| No left-right difference in width | Blocked: methods underspecified |
| Heights H1, H2, H3 taper | Reproduced (one combination) |
| Bottom edge most often concave | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's code is not public, so the pipeline follows the Methods and the readings the claims
file names; the centerline, slicing and resistance solver are equivalents of the paper's MATLAB
functions. After the first verification the centerline is cleaned of points off the vessel and
of repeats, and the PVS of each cross section is the two lobes beside the vessel. The ellipse fit surrounds the vessel, fit to the PVS and vessel together, as a reader
settled in answer to a question on the claims file
([`questions/000491.yaml`](../../questions/000491.yaml)). After the second verification no outcome changed. A path along the fitted centerline would give
counts inside the claim's range, so a change of cross-section-counts to reproduced is proposed for a
third round. The cleaned path of location E follows a side branch; without E,
fig8-ellipse-parameters and fig9a-heights-taper would both be partially reproduced. Among the findings about the data: the deposited vessel and PVS masks still overlap in
11 of 14 files; at E and F the PVS mask fills every plane below a depth; the vessel mask of E still holds its
branching vessels; the first published
version lacks the PVS masks of L, M and N; and the 2D images used to validate the segmentation are
not in the dandiset. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000491-raicevic-2023-01.yaml`](../../attempts/000491-raicevic-2023-01.yaml).

- `reproduce_raicevic_2023.ipynb`: the analysis. It takes about 29 minutes on four cores, most of
  it in the cross sections and the resistance solves.
- `pvs.py`: streaming the masks, the centerline and cross sections, the fits, the resistance solver
  and the distribution peak. Other notebooks on this dandiset can import it.
