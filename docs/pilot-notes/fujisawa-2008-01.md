# 000067, Fujisawa et al. 2008

No claims reproduced, five partially, seven not reproduced and four blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 16. The author then
changed `fig4-position-dependence` from not reproduced to blocked as
`methods_underspecified`, because the calibration the verifier asked for
showed that the criterion's test flags 30.0% and 75.0% of synthetic pairs
with constant efficacy, and wrote a criterion for `traj-diverge` that moved
it from blocked to partially reproduced; round 2 disagreed with that change,
the author proposed blocked as `data_missing`, and a third round agreed. The
paper reports the firing of neurons in the medial prefrontal cortex of rats
during an odor-place matching task on a maze, and the monosynaptic
connections between them. The channel map, the counts of rats and units, the
active fraction, field size, trajectory and odor selectivity, connection
rates, cell classes, the fall of connection probability with distance,
position dependence, facilitation and depression, and supralinear summation
were tested on eight working memory sessions from three rats, with units
placed on the prefrontal probe from their waveforms; task performance, the
divergence of trajectories and the example session EE.188 are blocked as
`data_missing`. Some outcomes rest on weak ground: in
`fig3-connection-rates` only the inhibitory rate is within tolerance, and
without the 34 of 74 inhibitory connections that mirror a peak in the other
direction none of the three rates is; `fig3f-distance` fails on a Spearman
test over eight bins that the 1400 micrometre bin (2 of 310 pairs) breaks,
with rho = -0.964 over 0 to 1200 micrometres; and with EE.088's units placed
by the conversion's block order the unit count is 631, within tolerance, so
`rats-and-units` fails on the count of rats. The author used the author
manuscript in PubMed Central, the verifiers could not fetch the full text,
and the supplement, which defines the measures of Figures 6 and 7 and the
thinning step of Figure 4, could not be retrieved.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
It holds three rats (EE, FF, GG) of the paper's four, and of the 13 working
memory sessions in the CRCNS session table EE.152, EE.165 and EE.188, the
paper's example session, are not in it, while EE.210 has no trial table or
position. The units table holds spike times only, with no channel, shank,
brain region, cell type or quality label, and mixes prefrontal units, CA1
units, multi-unit clusters and clusters of the sensor signals; units can be
placed only from their waveforms in the wideband signal, which EE.042 and the
ten sessions of 2008-06-27 (EE.080 to EE.089, among them EE.088) do not have.
The two position series are the x coordinates of the two head LEDs, in pixels
although stated in metres, the second is zero in every file and there is no y
coordinate, and the trial table lists only correct trials without saying so,
so task performance and where the trajectories diverge cannot be tested. In
rat GG the nose-poke sensors are on channels 65 and 66 and the CA1 probe on 70
to 101, where the CRCNS description gives 97 and 98 and 65 to 96, and the
sensor on 66 is active on trials labelled Right, so either the sensors or the
side labels of GG are swapped. Other findings: electrode locations are
"unknown", coordinates are missing, impedances are -1, and the electrode
groups are cuts of eight consecutive channels that do not identify the
probes; the layer recorded in each rat is not stated; the trial table's
stop_time is the paper's trial start, and left_or_right carries the
description of reward_time; the linearized position is stated in metres but
runs from 1 to 2, with 0 outside trials; in six files the spike times of unit
1 are not in ascending order; GG.063, a spontaneous alternation session in the
CRCNS table, has a trial table with left and right trials; every file's
session description is the paper's abstract and session start times are dates
at midnight; and no code of the paper's analysis is published.

The Methods' rank band for `fig4-position-dependence` was replaced by a mean
plus c times s.d. band after a first run of the rank version gave 1.0% and a
synthetic test showed that it could not detect a strong position-limited
coupling, with the rank result kept as a variant. Untracked files in the
repository root, which the author took to be sandbox placeholders, were left
alone. The author's points on the protocol: a channel map from outside
documentation that the paper does not rely on; a stated spread across
neurons used as the tolerance of a mean; values given by layer with no layer
known for each rat; three criteria written after a timing run printed
connection counts; a Methods test that cannot reach significance, which the
tie-break rule does not cover; no paper code, so the conversion code was read
to interpret the files; no rule for when the unavailable supplement defines
the methods; a label link that holds only after a correction; a per-rat
criterion that one rat cannot meet; and units that sessions of one day may
share.
