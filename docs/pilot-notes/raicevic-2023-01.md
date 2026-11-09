# 000491, Raicevic et al. 2023

Seven claims reproduced (all seven on an assumption), four partially (all four
on an assumption), eight not reproduced (all eight on an assumption) and three
blocked, one for missing data and two as methods underspecified. The first
verification round agreed with all 22 outcomes as they stood and the second
with all 22; one change of outcome was proposed after the second, and a third
round did not agree with it, so the outcome stayed. It pins version
0.230602.1307, the latest published one, as the earlier 0.230427.1809 holds no
PVS masks for locations L, M and N. The paper, Raicevic, Forer,
Ladron-de-Guevara, Du, Nedergaard, Kelley and Boster, "Sizes and Shapes of
Perivascular Spaces Surrounding Murine Pial Arteries", a Research Square
preprint, images 14 pial periarterial PVS segments (locations A to N) in 9
mice with 3D two-photon stacks, takes cross sections normal to the vessel
centerline and measures the PVS-to-vessel area ratio and the hydraulic
resistance of the segmented PVS, of three fits (ellipse, spline and
polynomial) and of the optimal elliptical annulus; the dandiset holds 14 NWB
files, one 3D stack per location in three channels with the final binary
segmentations of PVS and vessel. The claims were written from version 1 of the
preprint as served by PubMed Central (PMC9949243), without the version of
record, a PDF or Additional Files 1 to 6; the paper links no code, which is
MATLAB and not public. The open pipeline details were written once as steps P1
to P9 (voxel size, which centerline points were removed by hand, the median
PVS width of the edge exclusion and others), and each claim runs the
combinations of readings that bear on it. The check added, among other
changes, a second reading of the vessel area in the fits' area ratio (P5) and
a judgement of "very similar" against the paper's own annulus-over-ellipse
ratios, and left open the location tolerance of `area-ratio-per-location`, the
thresholds of `fig8-ellipse-parameters` and the test of
`left-right-no-difference`. All claims but the segmentation validation could
be tested from the deposited segmentations. Reproduced are
`fig5d-polynomial-closest-area-ratio` (70.7, 20.6 and 8.8% in 4 of 96
combinations), `ellipse-annulus-underestimate` (1.82 and 1.702 in one
combination of 48), `spline-resistance-five-times` (6.59 against 6.2),
`fig7-velocity-profiles`, `vessel-radius-peak` (29.50 um, within in 13 of 24),
`fig9c-pvs-two-lobes` (14 of 24) and `fig9a-heights-taper` (1.228, 0.820 and
0.305 in one combination of 48). Partial are `table2-fit-area-ratio-peaks` (at
most 3 of 7 values within), `fig6a-resistance-power-law` (-1.926, R2 0.922),
`fig5b-polynomial-closest-resistance` (at most 2 of 4 peaks within on linear
bins) and `fig9f-pvs-concave` (63.9 to 73.6% of values below 1, the peak never
within). Not reproduced are `cross-section-counts` (202 to 604 cross sections
per segment at 0.648 um, against 54 to 451),
`fig5a-pvs-area-scales-with-vessel-area` (slope 0.912, R2 0.176),
`fig5e-area-ratio-distribution` (median 1.226 to 1.565 against 1.88),
`area-ratio-per-location`, `fig6b-resistance-segmentation-peak` (median
5.28e15 to 6.87e15 against 3.84e15), `resistance-per-location`,
`fig8-ellipse-parameters` and `fig9e-pvs-width-asymmetry`.
`segmentation-validation-overlap` is blocked for missing data, and
`fig5bc-area-intersegment-variation` and `left-right-no-difference` as methods
underspecified, their criteria's readings splitting. Every tested outcome
rests on the stand-ins for the paper's manual steps: the longest skeleton path
cleaned of points off the fitted centerline, the PVS of a slice taken as the
two largest regions beside the vessel and planes the PVS mask fills cleared,
and the claims on the fits also on the polynomial region closed at the vessel
center height. The author's first run had 5 reproduced, 9 partially, 6 not
reproduced and 2 blocked. The author asked a reader whether the ellipse is fit
to the PVS alone or to the PVS and vessel together; the answer amended P9 to
the latter, and in the author-answers run `ellipse-annulus-underestimate`
became reproduced. Round 1 found that the centerline was 1.28 to 2.24 times
the distance between its ends, that the PVS of a slice was every PVS pixel in
the plane, that several outcomes rested on the P4 reading that leaves segments
empty, that the edge distance was measured from the skeleton point and that
the fits were solved at erosion 3 only; in reply the path was cleaned, the PVS
taken as the lobes beside the vessel, the filled planes at E and F cleared,
the fits solved at every erosion and whether fig5b may take logarithmic bins
went to a reader in `questions/000491.yaml`; five outcomes changed
(fig5e and fig6b to not reproduced, fig5bc to blocked, fig5d and fig9a to
reproduced). Round 2 found that the cleaned path still meanders (1.25 to 1.78
times its end-to-end distance in 12 of 14 segments), that E's path follows a
side branch and sentences the outputs did not support (one fig6b peak within
where there are three, Table 2 values printed nowhere, and the misquoted lobes
rule among them); in reply the text was corrected, a cell recomputing every
table without E was added (without E, fig8 and fig9a would be partially
reproduced) and a change of `cross-section-counts` to reproduced was proposed
from counts along the fitted centerline (223 to 427 at each segment's own
step). Round 3 did not agree, as those counts are scaled from the kept share
and not taken from slices, the reading is outside the claims file and the step
that passes was not measured (about 0.73 um would give a most of about 539),
so the outcome stays not reproduced and the analysis waits for a new attempt.
The clean run took 1,600 s at first, after a first development version of 44
minutes was restructured, 1,265 s after the author-answers run, 28.5 and 29
minutes after rounds 1 and 2 and 2161 s at the end. Deleting the author's
development pickles in the session's temporary folder was refused for lack of
approval, and the untracked files in the repository root were left alone.

The single-plane time-averaged 2D images and their segmentations, which the
Methods use to validate the 3D segmentation (at least 70% overlap), are not in
the dandiset, and the paper says its data are available from the corresponding
author on request. At E and F the PVS mask fills every plane below a depth (87
and 58 planes, 98 to 99% of the field) and 50 to 60% of the whole volume,
which the dandiset does not describe. The vessel mask of E holds a network of
branching vessels in one connected region, though the Methods say the branches
were removed by hand; after cleaning, 361 of its 939 points (0.648 um) are
kept, along a side branch, while the points removed run along the vessel with
PVS beside it. The vessel and PVS masks overlap in 11 of the 14 files (from 24
voxels at C to 344565 at E and 177417 at J), though the Methods say
overlapping pixels were removed, and the dandiset does not say which mask
should take them. For L, M and N the reference_frame gives a depth step of
0.648 um while the session descriptions say 1 micron; the vessel cross
sections at the stated step are close to round (median height over width 0.91,
1.08 and 1.13), so the descriptions appear wrong. The vessel channel (ChanA,
described as FITC-dextran) has an emission wavelength of 698 nm and the PVS
channel (ChanC) 525 nm, where the Methods put FITC-dextran in the green 525 nm
channel, and every imaging plane names GFP as its indicator. ChanB is
described as injected fluorescent microspheres, which the paper does not
mention, and L, M and N have no ChanB. The subjects of A to D are 573 to 603
days old in the files and most others 76 to 113 days, where the Methods say 8
to 12 weeks. The first published version, 0.230427.1809, holds no PVS mask for
L, M and N, a change the description does not record. Questions are put to the
paper's authors: which test found no difference between the left and right PVS
widths; how the median PVS width of the edge exclusion is measured; what shows
that PVS area varies much more between segments than along each; and, with the
code not public, which centerline points were removed, which PVS regions form
a slice's PVS, how the polynomial region is closed across the vessel and how
each fit's edge points are chosen.

The author's points on the protocol: running every reading multiplies the work
to up to 128 combinations per claim and with it the chance of a match by luck,
so all were run and the matching combinations counted; two readings could not
be run in full, P2 (b) with 438,100 points and more than 30 h of work, run for
the counts only and recorded as a deviation and not as `too_large`, and the
fits' resistances at erosion 3 only; the protocol does not say how to report
`measured` when nothing matches, so a stated reference combination was used;
for `left-right-no-difference` the claims file's rule for split readings
clashes with the protocol's rule that a claim of absence is judged on the
paper's test, and as the paper names no test the claims file was followed;
there is no rule for a claim that takes peaks from two claims binning
differently, so both peaks were paired under the same bins; and the result
cells and summary are markdown written after the run and copied into the
executed copy.
