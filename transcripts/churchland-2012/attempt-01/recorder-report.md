I ran `python tools/readme_row.py 000070 --write`, which added the row `| 000070 | Churchland et al. 2012 | 5 | 7 | 4 | 6 |` to README.md, and added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, claims and entry are unchanged. The repository root also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others), and I left them alone.

### 000070, Churchland et al. 2012

Five claims reproduced, seven partially, four not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim without
seeing the record and agreed with all 22; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports that the population
activity of premotor (PMd) and motor (M1) cortex in monkeys making reaches in
a maze task rotates in the plane found by jPCA, and that a rotational dynamics
matrix (M_skew) fits it nearly as well as an unconstrained one, while
simulated kinematic populations and muscle activity show no consistent
rotations. The direction of rotation across conditions and reach curvature,
the prediction of the phase from the preparatory state, the variance captured
by the jPCA planes and by PC2 and PC3, the angle between the state and its
derivative, the fit of M_skew, the rotation frequency, the shuffle controls,
the two arrays analysed separately and the two kinematic models were tested on
the J-array and N-array datasets, with the 192 per-electrode units each file
holds in place of the paper's sorted isolations. The six claims on the leech
and walking-monkey data, the single-electrode datasets, the EMG, the generator
model and the speed task are blocked as `data_missing`. Some outcomes rest on
weak ground: in `fig3ef-same-direction` jPCA orients the plane so that the net
rotation is counter-clockwise, so the fraction is also 0.963 to 0.991 after
shuffles 2 and 3; `suppfig3-shuffle-controls` fails on R2(M_skew), which the
supplement does not expect shuffles 2 and 3 to reduce; in
`fig3-phase-from-prep-state` shuffle 1, which has no rotation, scores 0.82 to
0.91; in `rotation-frequency` J-array reaches the range with windows starting
at -150 or -100 ms (1.31 and 1.45 Hz), where the paper chose a window per
dataset; and the angle peak of the two kinematic models depends on choices the
Methods leave open, with the velocity model peaking at 0.028 pi only with no
lead and no preparatory tuning. The lab's jPCA download page returned HTTP
403, so the method choices it leaves open were taken from a Python port, and
the Supplementary Information was taken from the publisher's site, as PubMed
Central served a bot page.

The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
It holds the paper's two array datasets but not the sorted isolations the
paper analysed (146 for J-array, 218 for N-array): its Units table has 192
units per file, one per electrode, and the seven single-electrode datasets,
the EMG, the leech and the walking-monkey data are not in it either, so six of
the paper's main findings cannot be tested. In nine of the ten files, all
written by the first conversion, the first entry of units/spike_times_index is
the true end of unit 0 modulo 65536, so unit 0 is cut short (in J-array 61030
of its 257638 spikes) and its remaining spikes open unit 1. In five Nitschke
files (ses-20090812, 20090819, 20090910, 20090920 and 20100923) the clock
restarts at recording segments after the first, as the conversion offsets only
one segment; trials overlap in time (2094 overlapping pairs in N-array) and
spike times go backwards at each restart, so spikes can be placed in trials
only by their storage order, which decodes reach direction in every segment.
Other findings: hand position is stated in metres with a conversion of NaN but
its values span about -220 to +165 and are in mm; the hand ends a median 35 mm
(Jenkins) and 52 to 53 mm (Nitschke) below the reached target in y while the
cursor lands on it, an offset the files do not describe; the Units table
carries only the default description and does not say whether its units are
sorted neurons, multi-unit activity or threshold crossings, and their number
and rates (8.8 to 300 spikes/s over trial time) are consistent with
channel-level activity; the dandiset does not say which of its ten sessions
are the paper's datasets, and the other eight are not described; and the first
conversion's code sets the year of every session date to 2009, so
sub-Nitschke ses-20090910, which is consistent with the N-9-10-2010 dataset of
Supplementary Figure 5, may be dated a year early.

In round 2 the verifier's copy printed 0.614 and 0.726 and 6 of 10 shuffle 3
runs reaching the J-array value for the cross-validated phase prediction,
against 0.615, 0.727 and 8 of 10 in the author's runs from the same code and
seeds; the source of the difference was not found, and the text now says the
count can move between runs. Untracked files in the repository that the author
did not create were left alone. The author's points on the protocol: criteria
that need values given only in figures; no rule on whether code read for
method choices, when the paper links none, belongs in `inputs`; no category
for control populations simulated from the data, whose free choices decide an
outcome; reported averages over datasets of which the dandiset holds only two;
whether an analysis may repair a format error; and a session that may be one
of the paper's datasets under the wrong date, used only as a variant.
