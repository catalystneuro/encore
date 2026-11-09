# 000004, Chandravadia et al. 2020

Ten claims reproduced, eight partially, four not reproduced and one blocked
on the dandiset, plus two claims using the earlier release (Faraut et al.
2018), both partially reproduced; both rounds agreed with every outcome.
The paper is a data descriptor, so most claims are about what the files
hold (counts, tables, codes, dates); the rest are the Figure 5 analyses of
visually and memory selective cells, which reproduce for the visually
selective cells and the ROC measures.

The dandiset was converted with CatalystNeuro's involvement (Ben Dichter
is a contributor). The most consequential finding is that the
`new_old_labels_recog` column is described, in every file and in the
paper, as 0 for old and 1 for new, while the data use 1 for old; the
paper's own code reads it correctly, but a user who follows the
description inverts every recognition analysis. Others: two pairs of
sessions hold identical spike trains for all their units, so 55 of 1864
units are repeats; eight sessions have fewer encoding trials than the 100
the paper describes; the spike times of 13 units are out of order and two
units hold every spike twice; electrode impedance is empty and some MNI
coordinates missing; age or sex differ from the paper's table for three
subjects; one session keeps the real day of the experiment, which the
paper says was removed; and the new sessions hold 325 units where the
paper says 288 were added. The memory selective and dual cell counts are
not reproduced under the Methods' test, but the paper's code, which uses a
different window and correct trials only, reproduces them exactly
(`code_mismatch`).

The author's points on the protocol: Methods that disagree with code that
reproduces the paper exactly; a stated spread used as a tolerance; the 10%
default on record counts in a data descriptor; claims for a paper that
describes data instead of reporting findings; counting a unit once when two
sessions share spike trains; a public input that refuses automated
download (Dryad); criteria written after a data check that is itself the
test; no default threshold for partial outcomes; and whether tables copied
from the paper count as inputs.
