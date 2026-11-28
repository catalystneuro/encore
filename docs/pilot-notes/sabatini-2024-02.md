# sabatini-2024, Sabatini et al. 2024, second attempt

Thirteen claims reproduced, 11 partially, 10 not reproduced and none blocked;
24 outcomes rest on an assumption, chiefly that trials are aligned on the
file's online movement onset and that hand positions are taken relative to the
start of the reach. The first verification round agreed with all 34 outcomes
as they stood, `fig7f-decoder-beats-standard` then blocked among them; the
author ran the decoders and moved it to partially reproduced. The second round
agreed with all 34, and nothing was proposed after it, so there was no third
round. It pins version 0.261122.2046, for which every file of the dandiset was
rewritten after the first attempt, `sabatini-2024-01`; the paper cites no
version. The paper, Sabatini and Kaufman, "Reach-dependent reorientation of
rotational dynamics in motor cortex" (Nature Communications 15:7007),
reanalyses Utah array recordings from PMd and M1 of two monkeys, J and N,
making 72 straight and curved maze reaches, and reports that activity on each
condition is a low-dimensional linear dynamical system (LDS) whose rotations
share frequencies of about 0.5, 1.5, 2.5 and 4 Hz across conditions while their
planes reorient with the reach, that the state space location predicts the
rotations, and that a model built on this (LDR) encodes and decodes reaches
better than standard models. The claims were written from the version of
record (PMC11325044) with its supplement and from the paper's code,
kaufmanlab/LDR-public at commit b65f28d, which loads preprocessed files
available only on request and was read for method details only. Reproduced are
the single-condition LDS fits (5 to 7 dimensions, 83.4% to 94.4%), the
temporal basis factorization (92.3% to 97.1%), its shuffle control and
recoverability, the jPCA variance, the prediction of rotations from rotations
and from the location, the location's distinctness from the rotations and its
relation to reach direction, LDR encoding, its advantage over standard encoders
and its sextant control, and LDR decoding (88.9% to 93.3%). Not reproduced are
the eigenvalue clusters (3 of 10 median pair frequencies within 10% of 0.5, 1.5
and 2.5 Hz), the eigenvalue AUC (0.580 to 0.717 against 0.51 to 0.58), the
single LDS over all conditions (77.3% to 82.6% against 46 to 66%), the
eigenvalues from kinematics (0.243 against 0.1), the duration warping, the
model comparison of Supplementary Figure 3, the dimensionality of the rotation
orientations and of the location, the jPCA variance correlation and the
absence of a drop without the output-potent dimensions (drops of 0.29 to 0.90
points, significant in every dataset). The basis frequencies are partial, with
3 or 4 rotation pairs and an offset in every dataset but only 6 of 14
frequencies within 10% of the paper's, and so are the plane alignment (13 of 14
rotations), the frequency segregation (35 of 36 comparisons) and the decoder
comparison, whose GPFA decoders were not run. The reconciliation with
`sabatini-2024-01`, run blind, found ten outcomes changed: six come down to
whether the factorization is fitted on -150 to +850 ms or on the whole -350 to
+850 ms window, `fig7f-ldr-decoding` to an error in the earlier attempt's
variance formula, and none to the dataset change, as the spike counts the
analyses use are the same in both versions except for Jenkins units 0 and 1.
The author had read the version's release notes, which list conversion fixes
linked to shenoy-lab-to-nwb issues #9 to #13, but saw no earlier results. Round
1 asked for the per-trial reading of reach duration in fig3i, a rerun on the
file's offline movement onset, a like-for-like held-out comparison for
Supplementary Figure 3, the Methods' normalisation before the basis of fig4d
and fig4f, a check of the kernel length scales and the standard decoders that
fit in memory; in reply all were run, the onset-dependent claims kept their
outcomes on the offline onset, and the held-out comparison favoured the
factorization in all four datasets and was put to a reader in
`questions/sabatini-2024.yaml`. Round 2 found many quoted numbers off in the
last digit, which the author traced to the verifier's copy having been run on
another machine, and some real errors (the fig3i seed spread, the fig4f ranges,
the offline fig3a count), which were corrected; the 15 claims the offline-onset
variant does not cover were marked as assumed, and the paper's
`removePotent.m` was found to centre each sample over the four kinematic
variables, as the notebook does. Notebook 1 ran in 37 minutes and notebook 2
in 8.4 at first, with peak memory 3.4 GB, 27 and 13.5 minutes after round 1 and
about 40 and 22 after round 2; the reconciliation's three notebooks ran in 49,
30 and 2 minutes. An early run with a fork-based multiprocessing pool hung
until its 50-minute timeout, and the first full run failed on two sessions
without `maze_condition`; both were fixed. The author's first run left the
version number in bold in the notebook 1 header, seen too late for another
46-minute run. For the reconciliation, `docs/pilot-notes.md` had no section
after pilot-14, and the repository's single commit made the recipe for the
earlier entry return the new one, so the earlier code was read from
`earlier-entry/`.

The dataset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
The units are unsorted threshold crossings, one per electrode (96 per array,
Blackrock unit code 0, as the units table now says), where the paper analysed
sorted single units and stable multi-units, 79 to 118 per array; the sorting is
not in the dandiset, every population analysis runs on the threshold
crossings, and the verifiers held this a plausible cause of the failed
dimensionality claims (major). In the Nitschke file M1 unit 170 fires above 100
spikes/s on 229 of the 2121 successful trials, all starting between 18902 and
22462 s, at a mean of 365.6 spikes/s on those trials against 31.9 spikes/s on
the others, and its largest mean rate over blocks of 50 trials is 13.7 times
its median block mean, against at most 2.5 for the other units, with nothing
marking it (major). The dataset holds no EMG, so Supplementary Figure 8 was run
with only the hand position and velocity dimensions removed. Eye positions are
labelled meters with a conversion of NaN and stored values of -331.2 to 369.4
(J) and -297.8 to 411.3 (N), and the trials tables of two Nitschke sessions
the paper does not use (2010-09-20 and 2010-09-22) have no maze_condition
column. Trials, spikes and hand share one clock, and the 72 conditions and the
trial counts (1595 and 2121 successful trials against 1469 and 2014) match the
paper. Of the first attempt's findings, the overlapping clocks of the Nitschke
file and the two spike trains in Jenkins unit 1's row are fixed (unit 0 now
holds 257638 spikes and unit 1 264946), the hand and cursor positions now carry
a conversion of 0.001, and the units table now says what its units are. In the
paper's code, idDynamics.m returns the training data as its approximation, so
crossValidateDimensionalityConditions.m scores every dimensionality the same,
where the Methods describe a projection score; the code for the kinematic
basis, the Figure 6e regression, GPFA, the single-trial kernel decoders, the
decoders' velocity-to-position step and the 250 ms warp is not in the
repository. Ten questions are put to the paper's authors: which movement onset
was used, whether hand positions were taken relative to the start of the
reach, which jPCA version and parameters, how large the kernel decoders'
training subset was and how the velocity outputs were turned into positions,
which trials were analysed, the penalty for the OU kernel encoders, how the
noise excursion angles of Figure 4c were computed, whether the Supplementary
Figure 3 values were cross-validated, the span of the time shuffle, and the
scale of the kinematic basis functions with the units of the rates given to the
OU kernel decoders.

The author's points on the protocol: the rule of five seeds for every random
result conflicts with the 60-minute notebook limit for heavy resampling, so the
extra seeds used fewer folds or repeats and were skipped on 7 claims; three
steps ran with fewer repeats than the Methods or the code, each recorded as a
deviation; it says nothing about what to do when the Methods and the code
describe different procedures and the code is broken, and both the Methods'
score and a working LDS score were run; any edit to the entry, even to
markdown, forces a full re-run, which cost two extra 46-minute runs; and it is
unclear whether a finding's `output` may point at a tag that several cells
share.
