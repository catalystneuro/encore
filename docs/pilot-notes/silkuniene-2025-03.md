# 001277, Silkuniene et al. 2025

One claim reproduced on the dataset (on an assumption), none partially, one not
reproduced and 15 blocked, 10 for missing data, three as
`methods_underspecified` and two for insufficient metadata. The first
verification round agreed with 14 of the 17 outcomes as they stood and the
second with all 17, and nothing was proposed after the second, so there was no
third round. It pins version 0.250701.1610, the only published version. The
paper, Silkuniene, Silkunas, Pakhomova, Semenov and Pakhomov, "MHz compression
of pulse packets facilitates remote focusing of electroporation" in
Bioelectrochemistry, delivers packets of nanosecond pulses through four needle
electrodes to monolayers of CT26 and CHO-K1 cells and measures YO-PRO-1 (YP)
uptake and propidium (Pr) staining along the diagonals of the electrode square,
and the dataset holds only the pulse-duration experiment of Figure 6. The
claims were written from the author manuscript (PMC12331426), which lists no
supplement, without seeing the figures; the paper links no code. Only the
Figure 6 claims could be tested, on the assumption that the Figure 6 wells are
the five plate rows that each hold one well of 300, 600 and 900 ns.
`fig6b-peak-900ns-not-significant` reproduces, 900 ns having the highest centre
YP (899 against 866 and 551 camera units) with no test significant (ANOVA p =
0.54), also with all 7 600-ns wells, in every choice of 5 of the 7 and with the
plate rows paired (repeated-measures ANOVA p = 0.071).
`fig6c-normalized-decline-similar` is not reproduced, every reading showing at
least one distance where two durations' normalized profiles are separated by a
gap longer than the error bars (52 of 96 gaps between 300 and 900 ns), whatever
the well selection. `fig6d-longer-pulses-sharper-peak` and
`fig6d-600-900-differ-from-300` are blocked as `methods_underspecified`, their
readings differing: the FWHM slope is negative under all 48 readings and
significant under 28 (p 0.0020 to 0.0037 with contiguous ROIs fitted to the 15
per-well values, against the paper's 0.003), and the block rests on leaving out
the two P1 row B wells, with either of which the slope is significant under no
reading. `fig6d-900ns-fwhm` is blocked only because it depends on that claim;
its own criterion would be met (1.69 to 1.71 mm with contiguous ROIs). The two
Figure 5 claims on the YP and Pr profiles are blocked as
`metadata_insufficient`, nothing linking the 600-ns wells to Figure 5's 0-mm
group, and the claims on raised electrodes, the packet-rate series of Figures 3
and 4, the burst-number series and CHO cells of Figure 7 and the thermometry of
Figure 2 as `data_missing`. The author's first run gave the two Figure 5 claims
as not reproduced on an assumption. The author asked a reader nothing, so the
answer and author-answers runs changed nothing. Round 1 disagreed with the two
Figure 5 claims, which moved to blocked, and with `fig6d-900ns-fwhm`, which it
gave as reproduced; that claim was kept blocked under the protocol's dependency
rule (Author, step 1.5) and the disagreement recorded. Round 1 also found that
the Pr channel was unchecked, that distances were rescaled with no unscaled
variant shown, that contiguous ROIs overlap and that the tests ignored the
plate rows; in reply the OME channel names, an unscaled variant, a paired
variant, per-well Pr profiles and fits with an offset were added. Round 2
agreed with `fig6d-900ns-fwhm` on condition that the rule is as quoted, asked
that the two fig6d blocks carry the assumed flag, which the attempt schema
does not allow on blocked outcomes so deviations were added, and found sentences
the outputs did not support (the "8 readings" of the offset fits, the 300-ns
FWHM range, the 1-mm p range, the plate ratio, where the fig6c gaps fall, the
scope of the unscaled variant, a stale status table and the README's well
count), all corrected. The author's run took about 1 h 15 min (19:35 to 20:47
UTC); during development the first footprint detector failed on faint wells and
was fixed by correcting the tile shading of the stitched images. The notebook
ran in 590 s at first, 791 s after the author-answers run, 776 s after round 1
and 851 s at the end.

The dataset holds only the pulse-duration experiment of Figure 6 (18 wells of
CT26 cells on three plates, 2 bursts (x4) with packets delivered with no
interval); the packet-rate series and controls, the raised-electrode wells, the
burst-number series and CHO cells and the thermometry are not in it, and the
paper names no other public deposit. It has 5 wells at 300 ns, 7 at 600 ns and
5 at 900 ns where the paper reports n=5 per duration, and nothing says which
five 600-ns wells were analysed, though the Figure 6D trend depends on it: with
the five plate rows the trend is significant under 28 of 48 readings, with all
7 it is absent (p 0.83 to 1.00). Nor does anything say whether the 600-ns wells
are also the 0-mm group of Figure 5, and Pr images exist also for three 300-ns
and three 900-ns wells. Every well's subject description says "Protocol
consisted of 9 packets of pulses delivered at 0.2MHz frequency", including the
300-ns, 900-ns and sham wells, where the dandiset description and the paper
give 18, 9 and 6 packets. The two 600-ns wells of plate P1 row B,
P1_20240926_B2 and P1_20240926_B3, show YP uptake over the whole electrode
array (YP at 6 and 7 mm 78% and 36% of the centre, against 3 to 11% in the
other 15 exposed wells) and Lorentzian FWHMs of about 18 and 5 mm, and B3 also
loses Hoechst-stained cells over the centre at 2 h and has a Pr image without a
central spot, with no reason given in the metadata. The Pr and Hoechst image of
well P2_20240925_B3 is deposited twice with identical pixel data. The OME
metadata give 12 significant bits per pixel, but the YP images hold values far
above 4095 (largest 25 x 25 pixel block means 3500 to 22600), with the unit
"n.a." and no scaling described. There are no electrode positions, ROI
coordinates or measured profiles, so the footprints had to be found in the
images, and the plate layout is recoverable only from the subject ids.
Questions are put to the paper's authors: which five 600-ns wells form Figure
6, and whether the 600-ns wells with Pr images are the 0-mm group of Figure 5;
how far apart the ROIs were placed along the diagonals; and whether the Figure
6D trend was fitted to the 15 per-well values or the 3 means, and whether it
was linear or logarithmic.

The author's points on the protocol: the rule that a claim depending on a
blocked claim is blocked (step 1.5) blocks `fig6d-900ns-fwhm`, which depends
only on the parent's fitting method, and it was followed with the values given
in the notes; the criterion blocks a claim when readings differ while step 1.6
lets the author adopt the best-supported reading, and the criterion was
followed; the clock check of step 2 does not apply to single-time-point images,
and a spatial check was used instead (the YP peak within 0.42 mm of the array
centre in 16 of 17 exposed wells); there is no rule for a dataset with more
recordings than the paper analysed and no record of which were used, and it was
treated as an assumption with every subset shown; and reduced images were
cached during development only, the notebook streaming everything.
