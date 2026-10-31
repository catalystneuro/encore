I wrote `docs/pilot-notes/000686-pakhomov-2023-01.md` and changed no other file. Nothing is committed. The other untracked files in the working tree (dotfiles, `.idea`, `.vscode`, `scripts`) were already there and I did not touch them.

# 000686, Pakhomov et al. 2023

No claims reproduced, none partially, four not reproduced and 16 blocked. The
first verification round agreed with 17 of the 20 outcomes and the second with
all 20, and a third round, held on the one change of outcome proposed after
the second, agreed with it. It pins version 0.240515.1909, the only published
version; the paper cites none. The paper, Pakhomov, Gudvangen, Mangalanathan,
Kondratiev, Redondo and Semenov in Bioelectrochemistry, focuses
electroporation of CHO-K1 cells to the centre of a quadrupole array of four
1.5-mm needles (CANCAN) by the interference of packets of 600-ns unipolar
pulses, measured by YO-PRO-1 (YP) uptake, with a Sim4Life field simulation
(Fig. 3), single cells imaged by confocal time-lapse (Fig. 4) and stitched
images of cell monolayers (Figs. 5 to 9). The claims were written from the
accepted author manuscript in PubMed Central (PMC10247516), with no supplement,
and the paper links no code. Only the four Fig. 5 claims could be tested, on
profiles measured anew from the 18 images, as no ROI measurements are
deposited; the Fig. 3 claim and the four Fig. 4 claims are blocked as
`data_missing`, and so are the eleven Fig. 6 to 9 claims, as their conditions
are not in 000686, though they appear to be in DANDI:000875, 001025, 001027
and 001028, which were not opened. `fig5a-trains-stronger` is not reproduced
because at the e3 end the trains do not exceed the packets under any reading
or ROI geometry (1138 against 1299 a.u., p = 0.558; p = 0.268 to 0.858 over
the other geometries). `fig5a-packet-center-enhanced` is not reproduced: the
e1 end exceeds the centre in all 4 dishes (ratios 1.17 to 4.22) but p = 0.137
to 0.195 in the main geometry. `fig5b-rotation-center-peak` is not reproduced,
both comparisons holding in 12 of 32 readings, on the record's reading that
both the paired and the unpaired test of O6 must hold; every difference goes
the way the paper says. `fig5c-normalized-contrast` is not reproduced on the
assumption of ROIs one step (about 65 um) wide, the most direct reading of
Methods 2.4, a near miss: 5 of 32 readings fail, all with the centre ROI
(p = 0.0529 to 0.0601 with the measured footprint, 0.0512 to 0.0824 with the
needle reading), while with ROIs three steps wide all 32 hold. The author's
first run gave fig5b and fig5c as reproduced on assumptions (the LOESS centre
and the unpaired test), fig5a-trains-stronger as partially reproduced and the
Fig. 6 to 9 claims as blocked by `other`, with a question to a reader on
marking them data elsewhere. Round 1 disagreed with fig5a-trains-stronger,
fig5b and fig5c, giving all three as not reproduced, and found that the Fig. 6
to 9 blocks should be `data_missing`, that ROI width changes outcomes, that the
trough was chosen and tested on the same dishes, that the ROI end depended on a
footprint radius estimated from intensity, and that the bright centre of 1P x
40 dish2 was unchecked. In reply the assumptions were withdrawn, six ROI
geometries were run under every reading, a leave-one-out trough and a
full-resolution crop of dish2 were added, and fig5c was blocked as
`methods_underspecified`, a disagreement with the verifier. Round 2 agreed
with all 20, asking that the record state its reading of O6 for fig5b and
calling the most direct ROI width the one-step square, and found sentences the
outputs did not support (a p range printed for the raw reading only, a 1T x 40
centre range given raw against a periphery range including background, the
age and subject count never printed, the e3 footprint said not to be visible);
these were corrected, helper checks on a synthetic image were added, and the
change of fig5c to not reproduced was proposed. Round 3 agreed, with caveats
that it is a near miss and that the 1P x 40 centre rests largely on dish2.
Questions on the reading of O6 and on the wording of O1 in the claims file
were added for a reader. The author's run took about 62 minutes (09:50 to
10:52 UTC); the first electrode detection was off by up to half a footprint
radius, caught on the overlay figure and refined, which made fig5b and fig5c
fail under the centre-ROI reading. The notebook ran in 377 to 413 s at first,
312 s after round 1 and 366 s in the last run.

The dandiset holds only the 18 monolayer images of Fig. 5 (40 Packets and 40
Trains, 4 dishes each; 1P x 40 and 1T x 40, 5 dishes each); the single-cell
time-lapse data of Fig. 4 and the field simulations of Fig. 3 are not in it
and were not found in any other dandiset. The paper's monolayer data are split
over five dandisets (000686 for Fig. 5, 000875, 001025, 001027 and 001028 for
Figs. 6 to 9), each naming the paper, but none names the others and the paper
names none of them. The files hold the stitched images only, not the ROI
measurements that the paper's profiles plot, so the figures can be rebuilt
only by placing ROIs anew. The species is NCBITaxon_9913 (Bos taurus) in every
file and in the dandiset summary, where the paper used CHO-K1 cells (Chinese
hamster), though the strain field says "cellline CHO", and the subject age is
P1D, which has no meaning for a cell line. The assets summary gives 36
subjects for 18 files with 18 distinct subject ids, and the image description
says the tiles came from a six-well plate, where the paper used 35-mm
glass-bottom dishes. The image has no pixel size; the tile geometry is
consistent with 0.65 um per pixel, at which the inner edges of the footprints
are 8.4 to 8.8 mm apart across the diagonal, consistent with the paper's
8.4-mm diagonal, and the footprints 1.15 to 1.44 mm across against the 1.5-mm
needles. The electrode footprints are not labelled, so which one is e1 is not
stated; the top-right footprint has the brightest outermost ROIs in all 8
non-rotated dishes. No file is deposited twice (the highest correlation
between two images is 0.815). In 1P x 40 dish2, bright pixels cover 44.6% of
the centre ROI, against 1.4 to 8.2% in the other dishes, in clusters that look
like labelled cells by eye. Questions are put to the paper's authors: whether
a profile's centre value is the ROI at distance 0 or the LOESS fit, and with
what span; whether the t-test within the same dishes is paired or unpaired;
which ROI is taken as 100% in Fig. 5C and whether each dish is normalized
first; and what ROI size, placement and background were used, as ROI width
decides fig5c.

The author's points on the protocol: the Fig. 6 to 9 data are public in four
other dandisets while the claims file sets their data to the dataset, and the
protocol forbids `data_missing` for public data while step 4 forbids outside
data the claims file does not name, so they were blocked as `other` with a
question to a reader; the protocol assumes the measured quantities are in the
files, where here the ROI measurements had to be rebuilt from images, adding
method choices that were recorded as deviations; step 2's shared-clock check
does not apply to single images; some criteria name no partial level, and
`partially_reproduced` was first used from the protocol's general definition;
for fig5b the claims file runs paired and unpaired tests (O6) but lists only
O1, O2 and O4 as readings that must hold, and the split was first settled by
assumption under step 1.6; and "do not download to disk" was met by keeping
8 x 8 block-mean copies in `$TMPDIR` during development, the notebook only
streaming.
