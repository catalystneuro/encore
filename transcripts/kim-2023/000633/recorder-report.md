I wrote `docs/pilot-notes/000633-kim-2023-01.md` and changed no other file. Nothing is committed. CatalystNeuro did not convert this dataset (its `catalystneuro` field is empty), so the second paragraph has no opening sentence about a conversion. The text of the note:

# 000633, Kim et al. 2023

Two claims reproduced, none partially, none not reproduced and five blocked on
the dataset, with one more reproduced and four more blocked that also need
outside data. The first verification round agreed with 11 of the 12 outcomes
and the second with all 12, so there was no third round. It pins version
0.231013.2226, the only published version; the paper cites none. The paper,
Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli and Pakhomov
in the International Journal of Molecular Sciences, electroporates monolayers
of bovine pulmonary artery endothelial (BPAE) cells with nanosecond pulses
through arrays of hollow needles and measures YO-PRO-1 (YP) uptake as the
direction of the electric field changes between pulses; the dandiset's title
names the experiment of Figure 4, a triangular array given trains of single
pulses on one base electrode or paired pulses on the two base electrodes in
alternation, at 833 kHz and 4 kV. The claims were written from the version of
record served by Europe PMC (PMC10341945), with no PDF, so the numbers printed
only inside the figures were not read; the paper links no code and says its
data are available on request. The three Figure 4 claims were tested; the four
Figure 2 claims, the three Figure 3 claims and the two Figure 5 claims are
blocked as `data_missing`. The paper's Sim4Life field map is not deposited, so
the field was computed here by a two-dimensional finite-difference solve from
the geometry of Methods 4.2 and 4.3 and the electrode positions measured in the
images, with the paper listed under `inputs`; the scale, 0.654 um per pixel,
comes from the 1.5 mm needles. `fig4a-single-pulse-follows-field` reproduces on
an assumption, with E1, the pulsed electrode, taken as the lower-right base
electrode (base_a): over 2627 ROIs YP and the computed field have Spearman
rho = 0.666, and 0.654 (p = 0.00053, 24 ROIs) on ROIs thinned to 2 mm spacing,
and the order of the three electrode neighbourhoods matches (base_a 649.8,
base_b 262.6, apex 82.2); with E1 as the other base electrode rho is 0.424 to
0.510 and the order never matches. `fig4bc-paired-pulse-focal-apex` reproduces,
flagged as resting on the single-pulse file being the image of Figure 4A: in
the paired-pulse image the apex/base ratios are 3.31 and 8.11 at 100 um and
2.69 and 6.10 at 500 um, against 0.051 to 0.200 in the single-pulse image.
`fig4-comet-shape` reproduces on the assumption that objects bright in the
MemBrite channel are not part of the monolayer; the literal maximum (3999) lies
on one such object and leaves the regions empty, while with those pixels left
out (0.54% of the region) the maximum is 1063 and the region reaches further
toward the base than across the line at half (1755 against 1315 um) and at a
quarter maximum (3929 against 1749 um), though at half maximum its full extent
along the line is smaller than across it (2446 against 2592 um), so the pass
there depends on the reach measure. For information only, the two Figure 4
images give an 833 kHz curve with 5.8-fold cancellation near 168.7 degrees,
against the paper's 20-fold, and a crossing of 100% at 128.4 degrees. The
author asked a reader no questions, so the answer run and the following author
run changed nothing. Round 1 agreed with 11 of 12; it would give the comet
claim as partially reproduced, as the literal maximum fails and the notebook
never examined the object under it, and it found that the single-pulse file's
description gives another exposure, that E1 was chosen from the uptake under
test and that the Spearman p-values treat contiguous ROIs as independent. In
reply the object was shown at full resolution in both channels (a blurred disc
about 105 um across, YP median 14577 and MemBrite 5266 against 305 and 255
around it), the MemBrite rule was added at 5, 10 and 20 times the dish median,
the smoothing was masked, the test was run on thinned ROIs and E1 was taken from
the published Figure 4A; the outcome was kept and the disagreement recorded.
Round 2 agreed with all 12, changing its view of the comet claim, and found that
a deviation saying the extents along and across the line agree was wrong, that
"one object" is left out where the rule leaves out many, that the placement of
E1 in Figure 4A is not shown, as the deposited images do not keep one
orientation, and that fig4bc should carry `assumed`; these were corrected and
fig4bc was flagged. In that revision the author mapped the deposited images
onto the published Figure 4 outside the entry, as the entry check refuses code
that reads an image file: the paired-pulse file matched Figure 4B turned by 180
degrees and not mirrored, while the single-pulse file did not match Figure 4A
in either orientation (at most 0.03), which, if it holds, would leave both
fig4a and fig4bc blocked in a later attempt; this is disclosed as not verified,
and no change was proposed. The author's run took about 31 minutes (05:47 to
06:18 UTC), with only a NaN-rounding error and a YAML quoting error fixed during
development. The notebook ran in 184 s at first, 239 s after the answer, 211 s
after round 1 and 154 s in the last run.

The dandiset holds only the two whole-dish images of Figure 4; the ROI
measurements of Figure 2 (n = 3 at 1 Hz and at 833 kHz), the square-array
experiments of Figure 3 (n = 6 per group), the strobe imaging of Figure 5 and
the field simulation of Methods 4.3, on which the paper's quantitative findings
rest, are not deposited, so nine of the twelve claims cannot be tested. The
session description of Single-pulse_trains describes another experiment ("4
co-directional paired-pulse (600 + 600 ns) trains ... 770 kHz, amplitude 10
kV/cm"), the settings of Figure 3, while its image shows a triangular array
with the single-pulse pattern of Figure 4A, and two of the three tested
outcomes rest on taking it as Figure 4A. Each image is stored as an
ImageSeries with data of shape (22323, 22323, 2) and a rate of 2 Hz, so a
standard reader sees 22323 frames of 22323 x 2 pixels where the data are one
stitched image in two channels. No pixel size, channel names or intensity unit
(unit "n.a.") are stored, the channel order is given only in free text, and the
file does not say which base electrode was pulsed in the single-pulse image.
The session description of Paired-pulse_trains gives 2 kV where the paper gives
4 kV for both Figure 4 images; the field model gives 4.2 to 9.7 kV/cm on the
bisecting line at 4 kV, close to the 5 to 10 kV/cm of Section 2.1, and half that
at 2 kV. The image description says the tiles came from a six-well plate, where
the paper used 35 mm glass-bottom dishes, the subject age is P1D for a cell
line, and each subject is a condition. The brightest YP in the paired-pulse
image lies on an object about 105 um across, 2.5 mm from the apex electrode,
bright in both channels and out of focus, likely debris above the monolayer,
and a maximum taken without leaving it out is about four times the brightest
uptake of the monolayer. Questions are put to the paper's authors: whether
Single-pulse_trains is the image of Figure 4A and which of its base electrodes
is E1, whether Figure 4A's image can be deposited if it is another file, and
how agreement of uptake with the field map and the comet-shaped region were
judged.

The author's points on the protocol: a claim needing two conditions where only
one kind of data exists, and the rule blocking claims that depend on blocked
claims, which hides `fig2-60-fold-co-counter` though it needs only 833 kHz, so
all Figure 2 claims were blocked as `data_missing`; a `with_inputs` claim whose
outside input is not public but can be recomputed from the paper's geometry,
which the protocol only says to block, and the field was recomputed and recorded
as a substituted model; a missing label that leaves a criterion's readings
disagreeing, where it is unclear whether that is `metadata_insufficient` or an
assumption, and the assumption was adopted with both assignments shown; step 2's
shared-clock check does not apply to still images; and the protocol has no rule
for robustness choices inside a criterion, such as a maximum broken by one
outlier, which was treated as a reading under step 1.6.
