# silkuniene-2025, Silkuniene et al. 2025, fourth attempt

Nine claims reproduced, five partially, four not reproduced and ten blocked,
eight for missing data and two as `methods_underspecified`; two reproduced
outcomes, `fig4b-40-fold-ratio` and `fig7-offtarget-40-50-fold`, rest on an
assumption about which electrode footprint gives the background. It is the
first attempt on all four of the paper's dandisets together, under one claims
file for the paper written under pilot-14, which replaces the three
per-dandiset files of pilot-10; it pins 001047 and 001276 at 0.250701.1609 and
001277 and 001284 at 0.250701.1610. The first verification round agreed with
24 of the 28 outcomes as they stood and the second with 27, disagreeing on
`fig6d-longer-pulses-sharper-peak`; after a reader answered two questions,
seven changes were proposed and a third round agreed with six. It did not
agree that `fig3bc-rate-suppresses-off-target` is reproduced, as the Fig. 3B
legend fixes the pooling of the diagonals, under which the result depends on
the footprint, so the claim stays blocked for missing data where the verifier
would block it as `methods_underspecified`. The paper, Silkuniene, Silkunas,
Pakhomova, Semenov and Pakhomov, "MHz compression of pulse packets facilitates
remote focusing of electroporation" (Bioelectrochemistry 166, 109016), delivers
packets of nanosecond pulses (CANCAN) from four needle electrodes to cell
monolayers and reports, from YO-PRO-1 (YP) and propidium (Pr) uptake, that at
a packet rate of 0.2 MHz electroporation is focused into a spot at the array
centre, 40 times the uptake near the electrodes, that killing stays at the
centre, that the spot narrows with higher packet rates and longer pulses, and
that the peak grows with the number of bursts, its sharpest FWHM 1.1 mm. The
claims were written from the accepted author manuscript (PMC12331426), without
the figures; the paper has no supplement and links no code. Reproduced are the
killing at the centre, the Gaussian Pr and Lorentzian YP profiles, the
reversible zone from about 2 mm (2.08 mm), the 900-ns peak not differing
significantly, the 900-ns FWHM (1.754 mm), the sharpest peak at one burst
(1.12 mm), CHO cells replicating CT26, and both centre to near-electrode
ratios, on weak evidence, since the footprint choice alone moves the 6-mm
ratio of means of Fig. 4B from 31.2 to 114.9. Partial are the central
enhancement and the Lorentzian fit of Fig. 3, held on two of the paper's packet
rates, the Fig. 5C zones without the nuclear part, the linear growth of the
peak with bursts (the CT26 slope has p below 0.001 in 38.4% of subsets of the
paper's size) and the CT26 saturation. Not reproduced are the weakening of the
centre with raised electrodes (48.7% and 28.9% of the 0-mm value at 1 and 2
mm, only the 2-mm drop clearing the error bars), the YP spot slightly larger
than the Pr spot (FWHM ratio 0.748), the similar normalized decline across
pulse durations, and the narrowing with pulse duration, which holds (p 0.0008
to 0.0058) only when wells B2 and B3 of the seven 600-ns wells are left out,
B3 for its broad profile, the quantity under test. Blocked are the field
simulation, the heating, the packet-rate trends of Figs. 3 and 4, and the 600-
and 900-ns comparisons with 300 ns and the FWHM against bursts, whose outcomes
change with the footprint. The author's first run gave 10 reproduced, 4
partially, 3 not reproduced and 11 blocked. Round 1 asked for the August 2024
wells, which match the paper's n, every footprint as background, all 21 ways
of choosing five 600-ns wells and subsets of the paper's size for Fig. 7; in
reply `fig5-raised-electrodes-weaken-centre` moved to not reproduced,
`fig7be-center-linear-with-bursts` to partial and `fig7-offtarget-40-50-fold`
to reproduced. Round 2 found that B3 does peak at the centre, so the record's
"no central peak" was removed, and that the "9 packets" finding rested on a
fixed string in a print statement, now parsed from every file. The reader's
answers added 001276 to four Fig. 3 and 4 claims and made the background
footprint an open reading, (i) to (iv). The `entry.py` check crashed in the
author-answers and round-3 runs because the blind checkout had no
`attempts/silkuniene-2025-03.yaml`, and was run with that file skipped; five
schema errors remain, none from round 3. The reconciliation with
`silkuniene-2025-03`, which used 001277 alone, found the attempt blind, one of
eight earlier findings partly fixed by this attempt's wider scope and seven
still present. The author's run took about 2 h; the notebook ran in 28 min at
first, with peak memory 2.75 GB, streaming 46.7 GB of images, and in 2744 s at
the end.

DANDI:001047, which cites the paper, holds images from a 3.8-mm array with a
3.2-kV first pulse, not the paper's 15.3-mm array with 7.2-kV pulses. Of the
packet-rate series of Figs. 3 and 4 only the 1-Hz, 0.2-MHz and control wells
are deposited, in 001276, whose description (0.2 MHz, 1 to 6 bursts) does not
mention the 1-Hz and control wells; the 1-kHz and 10-kHz wells are in none of
the four dandisets, and neither are the field simulation, the thermochromic
film images or the high-resolution images of Fig. 5C. Several groups hold more
wells than the paper reports, with no record of which it used: 001284 has 12,
11 and 11 YP wells at 0, 1 and 2 mm (paper n = 6 to 7), 001276 has 5, 8, 7 and
8 CHO wells at 1, 2, 4 and 6 bursts (paper n = 4) and 6 CT26 wells at 2 bursts
(paper n = 3 to 5), and 001277 has 7 wells labelled 600 ns (paper n = 5). Of
these, P1-20240926-B2 has its YP spot 5.39 mm from the array centre, against
at most 1.21 mm in every other 0.2-MHz CANCAN well with footprints, and B3 has
YP at 3 and 5 mm at 46% and 35% of the centre, against at most 13% and 9% in
the other wells of 001277. Every 001277 file states "9 packets of pulses
delivered at 0.2MHz" whatever the pulse duration, where the description and
the paper give 18, 9 and 6, and two 001284 Hoechst files state 900 ns in wells
whose other files state 600 ns. The descriptions and files give a 10-mm
inter-electrode distance, which matches none of the paper's distances. The
FITC image of 001284 well P1-20240828-A3 is 98% zero pixels, a pre-exposure
DAPI file of 001276 holds only zeros, and the Cy3-DAPI image of 001277 well
P2-20240925-B3 is deposited twice. In 001277 the OME metadata of the 13
Cy3-DAPI files give 12 significant bits while the values reach 25073 (Cy3) and
65535 (DAPI), the unit is "n.a." in all 49 files, and no file gives electrode
positions, ROIs or profiles, the plate and well appearing only in the subject
id. Three questions are put to the paper's authors: whether the regressions of
Figs. 6D and 7 were fitted to individual experiments or group means, which five
600-ns wells form the Fig. 6 group and what B2 and B3 received, and where the
ROIs were placed and which footprint gave the background.

The author's points on the protocol: it does not say whether to test a claim
on a dataset its `datasets` field does not list, and those claims were blocked
on 001047 with the 001276 wells shown as a variant; criteria that need a result
under every reading do not say what to do when the named readings disagree, and
the better-supported reading was adopted as an assumption; it gives no rule for
groups holding more wells than the paper, and all wells were used except where
the paper's n matched a visible anomaly; and `tools/entry.py` needs pyyaml,
jsonschema and nbformat, which the system Python lacked, so it was run with
`uv run --no-project --with`.
