# 001047, Silkuniene et al. 2025

No claim reproduced, one partially, eight not reproduced and 11 blocked. The
first verification round agreed with 17 of the 20 outcomes and the second with
all 20, so there was no third round. It pins version 0.250701.1609, the latest
published version; the paper cites none, the draft has the same 88 assets and
the first version had only the 54 CT26 files. The paper, Silkuniene, Silkunas,
Pakhomova, Semenov and Pakhomov, "MHz compression of pulse packets facilitates
remote focusing of electroporation" in Bioelectrochemistry, exposes CT26 and
CHO-K1 monolayers to CANCAN packets of 600-ns pulses from four needle
electrodes in a square with 15.3-mm diagonals, compares packet rates from 1 Hz
to 0.2 MHz, pulse durations of 300 to 900 ns, electrodes raised 1 or 2 mm and
burst numbers up to 6 bursts (x4), and reports that 0.2 MHz packets give a
sharp central spot of YO-PRO-1 (YP) uptake with about 40-fold suppression near
the electrodes. The claims were written from the NIH author manuscript in
PubMed Central (PMC12331426), without the version of record or the figures; the
paper links no code. The dandiset holds only 1 Hz and 0.2 MHz, so the rate
claims were tested on one comparison, and the burst labels (x1, x2, x3, x5)
were read as repeats after the first burst, making x1 the paper's 2 bursts
(x4) and x5 its 6 bursts, an assumption marked on every tested claim;
the other reading, the label as the total, is shown throughout, with 1 Hz x2
against 0.2 MHz x1 and x3. `fig4b-centre-no-rate-effect` is partial: centre YP
does not differ between rates at x1 (1.0 +/- 21.8 against -1.4 +/- 6.3 a.u., p
= 0.93), but neither rate stains the centre and no 1 kHz or 10 kHz comparison
can be made. `fig3a-centre-enhanced` is not reproduced under both label
readings, the 1 Hz profile peaking 6.5 to 7 mm from the centre and the 0.2 MHz
wells being essentially unstained (centre -1.4 a.u.). `fig3bc-rate-suppresses-off-target`
is not reproduced, 0.2 MHz being below 1 Hz at 6 and 7 mm (9.1 against 152.5
and 4.9 against 174.0 a.u.) with a gap beyond the longer error bar at neither,
and `fig4b-near-electrode-decline` is not reproduced at x1 on the reading of
the error-bar rule (F8) as the longer arm, and would be reproduced under the
shorter-arm reading. `fig3-lorentzian-profile` (1 Hz R 0.36 to 0.72, every
0.2 MHz fit at the 100-mm width bound), `fig3-tail-deviation-falls-with-rate`,
`fig4b-40-fold-ratio` (-0.29 to -0.15 at x1, no label and reading giving 36 to
44), `fig5ab-yp-spot-slightly-larger-than-pr` and `fig5b-gaussian-pr-lorentzian-yp`
are not reproduced, the two propidium (Pr) claims assuming the electrodes
touched the monolayer, which the data cannot check. Nine claims are blocked as
`data_missing`: the film thermometry of Figure 2, the 1 kHz and 10 kHz rates of
Figure 4C, the 300- and 900-ns pulses of Figure 6, the full-resolution Hoechst
images of `fig5c-nuclear-yp-centre`, and the CHO burst series of
`fig7be-peak-grows-with-bursts` and `fig7cf-fwhm-bursts`, whose CT26 halves were
tested and decide nothing (slope of centre YP p = 0.085 and 0.051, no FWHM slope
positive with p < 0.05 in 72 combinations). `fig5-raised-electrodes-weaken-centre`
and `fig7-sharpest-one-burst` are blocked as `metadata_insufficient`, no file
giving the electrode elevation and the labels not settling whether a 1-burst
well exists. The author's first run compared the rates at every label both
share (x1 and x5), giving partial where a claim held at one, and gave 1
reproduced, 1 partially, 7 not reproduced and 11 blocked, with fig3-tail as
partial, fig4b-centre as reproduced and fig5-raised and fig7-sharpest as
`data_missing`. The author asked a reader no questions, so the answer run and
the following author run changed nothing. Round 1 disagreed with fig3-tail,
whose x1 result measured deviation from a 0.2 MHz fit stuck at the width bound,
with fig4b-centre, and with fig7-sharpest, which it gave as not reproduced if
x1 is one burst; it also found that x5 is not a reading of 2 bursts and 1 Hz x2
was never analysed, that the F8 rule was read as the mean of the two arms
without alternatives, that the CT26 halves of Figure 7 were untested, that
14 areas were never shown and several had wrong centres, and that the Hoechst
images exist. In reply the labels were read as repeats after the first burst,
three F8 readings were shown, fig3-tail became not reproduced and fig4b-centre
partial, fig5-raised and fig7-sharpest were blocked as `metadata_insufficient`
(the disagreement on fig7-sharpest kept on record), and the Hoechst images were
found to be taken at 10:35, before the YP (12:49) and Pr (14:24) images. Round
2 agreed with all 20, withdrew its round-1 reason for fig5c, and found two more
misplaced areas in the deciding x1 groups, a `data_missing` finding that
counted 11 blocks where two are not for missing data, a background by image
type printed nowhere, and a duplicate check over only 121 same-condition pairs;
the two areas were flagged and the x1 claims shown without them (the fig3a
control part then holds, no outcome changes), and the rest was corrected. The
author's run took about 2 h 40 min and finished at 05:18 UTC; one development
run timed out after an hour on a duplicate check over every pair of images,
which was cut to pairs of the same condition. The notebook ran in 10.2 min at
first, mostly streaming 42 images (11.5 GB), 391 s after the answer, 410 s
after round 1 and 359 s after round 2.

The dandiset's 0.2 MHz CANCAN wells do not show the paper's main result: at x1
they are unstained everywhere (group-mean profile within 32 a.u. of background),
and at x3 and x5 broadly stained, with a centre to near-electrode ratio of 1.4
to 4.0, so its images may be other experiments than those of the paper's
figures. The dandiset description and every file's protocol text give a 3.8-mm
electrode spacing, a 3.2-kV first pulse and 75, 50 and 25% steps, where the
paper used a 15.3-mm array, a 7.2-kV first pulse and 16-pulse packets falling
by 12.5% per phase; the CT26 images show footprints at the paper's spacing
(best match 6.1 mm from the centre against 6.4 mm, over 52 two-well areas), and
if the wells were exposed at 3.2 kV they are not the paper's 7.2-kV
experiments. The dandiset holds CT26 monolayers at 1 Hz and 0.2 MHz and CHO
monolayers with one burst label, and no images at 1 kHz or 10 kHz, no 300- or
900-ns pulses, no thermochromic film images and no CHO burst series. The burst
number is given only in the subject label, all but one CT26 subject saying
"Unknown repetitions" and the protocol text saying only that the protocol "was
either repeated 2, 3, or 5 times", without saying whether the first application
counts. The CT26 files state no pixel size (the `resolution` attribute is 96 in
CT26 files and 0.1 in CHO files), and the images are on two scales without
saying so: whole-well images fit the 35-mm well at 1.625 um per pixel and
two-well images the electrode spacing at 3.25 um per pixel, the whole-well
images matching the spacing 9% above the paper's geometry, which was not
resolved, and their backgrounds (mean 2628 a.u., 7 YP areas) differ from those
of two-well images (mean 332, 45 YP areas), so their arbitrary units differ.
The 12 CT26 Hoechst images were acquired before exposure and at an inferred
3.25 um per pixel, half the resolution of the 4x camera. The dandiset holds
more wells per condition than the paper reports (6 CT26 1 Hz CANCAN wells at
x1 where the paper's S1 has n = 3 per rate) and a CHO set at 1 Hz the paper
does not report, without saying which wells the paper used; no well was found
deposited twice (peak normalised cross-correlation at most 0.039 over all 1654
pairs of areas in the same channel). No file gives the electrode elevation, and the CHO files use
session_start_time 2024-12-11, the conversion date, where their OME metadata
give acquisition on 2024-08-14. Questions are put to the paper's authors:
whether the subject label counts the repeats after the first burst or all
bursts, and which wells make up the 2 bursts (x4) sets of Figures 3 to 5;
whether the CT26 wells were exposed at 7.2 or 3.2 kV; whether the wells imaged
for propidium on May 24 2024 had the electrodes touching the monolayer; in
which footprint the background ROIs were placed and how the array centre was
located; and which error bar the gap must exceed when the two differ.

The author's points on the protocol: no rule says how to judge a claim whose
condition, here the burst number, cannot be matched to the dataset's labels;
claims over every rate or a trend over rates can only be partly tested when
some conditions are missing, and the rates present were tested with the
missing ones recorded as deviations, claims whose comparisons were all at
missing rates being blocked; step 2's clock check does not fit single
time-point images, and the condition labels and sides were checked against the
stain patterns instead; and image data with no annotations need a way to place
regions of interest, which was automated with a template match and a fallback
and shown in a figure for the verifier.
