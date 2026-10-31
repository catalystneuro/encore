# 000632-kim-2023

Tests the findings of Kim et al. (2023), "Control of the Electroporation Efficiency of Nanosecond
Pulses by Swinging the Electric Field Vector Direction" (Int J Mol Sci 24, 10921,
doi:10.3390/ijms241310921), on DANDI:000632 version 0.231012.1930.

The dandiset holds the square-array experiment of Figure 3: one stitched whole-dish image per dish,
with a MemBrite and a YO-PRO-1 channel. `epimg.py` streams the images chunk by chunk, locates the
four electrode footprints, and measures YO-PRO-1 in the 200 um ROI at the center of the array and in
the footprints. `reproduce_kim_2023.ipynb` runs the tests of the claims file.

Of the five Figure 3 claims, three are reproduced (no difference between co- and cross-directional
pulses at 1 Hz, none between 770 kHz and 1 Hz for cross-directional pulses, and the conclusion that
follows from the first) and two are not (the 770 kHz enhancement of co-directional pulses and the
co over cross difference at 770 kHz go the paper's way but are not significant). The claims on
Figures 2, 4 and 5 are blocked, as their data are not in the dandiset.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Run with `python tools/entry.py run entries/000632-kim-2023` (about six minutes).
