# 000727, Brezovec et al. 2022

Eight claims reproduced, five partially, one not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it gave
partially reproduced for `fig5c-global-below-threshold`, as the pass under
one reading rests on r = 0.013 with a p-value that treats autocorrelated
samples as independent. The author kept reproduced and added a null of 200
rolls of each fly's behaviour in time, against which the weakest correlation
has p = 0.025 (null 95th percentile 0.010), and round 2 agreed. Round 1 would
also have blocked the four region-level claims as `data_missing`; the author
kept `metadata_insufficient`, as the voxel data are deposited and only their
labels are missing, and round 2 accepted it. Round 1 also found a wrong
denominator in reading (b) of `fig2c-fraction-correlated`, which moved 54.9%
to 53.5% and no outcome. Round 2 agreed with all 20 and nothing was proposed,
so there was no third round. The preprint reports that whole-brain imaging of
nine walking flies shows activity correlated with forward and turning
velocity across much of the brain, organized by neuropil and mirror-symmetric
for forward velocity, that linear models on the principal components predict
behaviour with weights stereotyped across flies, that turning raises activity
on one side and lowers it on the other, and that peak correlation times range
from leading to lagging behaviour, with lagging voxels broader in time. The
dataset structure, the share and tuning of correlated voxels, the symmetry,
the PC structure, the ridge R2 and its relation to movement, the weights, the
unique variance of forward velocity and walking state, the below-threshold
correlations of the demixed regions, the ipsilateral and contralateral
changes, the peak time range, lag against width and the ipsilateral lead were
tested on 12 of 91 planes with 6 x 6 voxel blocks in place of supervoxels.
The four region-level claims are blocked as `metadata_insufficient`, the
tdTomato control as `data_missing` and the supervoxel number sweep as
`too_large`. Some outcomes rest on weak ground: `fig6-peak-time-range` gives
0.32 s with behaviour at the volume midpoint, but 0.58 s at the volume start
and 0.50 s with each plane's median removed, so only the lag of more than 1 s
is robust; `fig5c-global-below-threshold` holds under reading (b) only, with a
left region of 4 blocks; and in `fig2-symmetry` a left-right flip of fly_105
is not excluded. The author used the full text of bioRxiv version 1, as the
Current Biology version is paywalled, and took parameters where the Methods
are silent from the paper's code at commit 8e2b275.

The dandiset was converted by CatalystNeuro (catalystneuro/clandinin-lab-to-nwb).
The processed volumes are registered into the Functional Drosophila Atlas, a
space from a later paper of the lab, while the preprint analyses its data in
its own mean brain, and the dandiset holds no neuropil labels, atlas or
template for that space, nor the paper's mean brain and registered atlas, so
none of the region-level results (Figures 2E to I, 3, 6E to G, 7) can be
tested; nor does it say how the FDA series relates to the preprint's analysis
space. The per-plane acquisition times are not in the files, which give only
a volume rate, and sampling behaviour at the start in place of the middle of
each volume changes the correlated share of the brain from 31.1% to 39.2% and
the 99th percentile of forward-velocity lead from 0.32 to 0.58 s. The
supervoxel labels, the z-depth maps and the motion-corrected tdTomato channel
are not deposited. The processed series has grid spacing 1, 1, 1 in unit
"unknown", and nothing states which half of the volume is the fly's left.
Imaging and FicTrac both start at 0 s, as the conversion code set FicTrac
timestamps to a uniform 50 Hz from 0 because synchronisation data were
missing, which the dandiset does not say; the data are consistent with a
shared start (brain-wide activity follows walking speed by 0.4 to 0.8 s in
every fly) to within a few hundred milliseconds. Every FicTrac SpatialSeries
has unit "meters" and conversion 0.0045 (the ball radius), while most hold
angles in radians, and SpatialSeriesRotationDeltaError, described as an error
in radians, has medians of 6067 to 10,435. Other findings: the paper's code
computes the walking state with np.sqrt(a, b), which reduces it to forward
velocity alone, and the two versions mark 47.2% and 57.3% of time points as
walking; the Methods cite Figure 3F and 3G for panels in Figure 4, and Figure
3G is the Nodulus in the Results and the Ellipsoid Body in the legend; and the
preprint says the data were deposited at Dryad, where no record was found,
while the dandiset links neither Dryad nor the analysis code, which was found
as ClandininLab/brezovec_volition_2023 under a different title.

The notebook ran in 483 s in the first clean run and in 12.3 minutes in the
latest run. h5py over the network read at 2.6 MB/s, so the helper reads the
gzip chunks by HTTP range requests at about 98 MB/s, matching h5py in all
nine files; bioRxiv rate-limited the downloads and after round 1 the paper
could not be fetched again, and the GitHub API reached its limit, so the
repositories were cloned with git. Round 2 found statements the outputs
contradicted (the README run time, the time to stream the 12 planes, and a
round-1 response saying the lag of more than 1 s held in every plane from 38)
and a flip check, the overlap of each brain mask with its mirror, that cannot
detect a flip; these were corrected and the check replaced with leave-one-out
maps. Untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: a paper that names no
code repository, with the code found by search under another title; outside
resources the dandiset's processed data depend on but the paper does not
use; no rule for testing on a sample of a dataset too large to stream; where
the data check ends when prototypes are needed to find the left-right axis; a
clock check that cannot resolve the sub-volume alignment some claims need;
no definition of partially reproduced for a single expected value; what to
record as measured when no reading matches; following code that tunes on test
data; and a default 10% tolerance, kept for "approximately 0.3", which is
strict.
