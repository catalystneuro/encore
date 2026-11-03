# 001517, Semenov et al. 2026

Five claims reproduced (all on an assumption), two partially (one on an
assumption), four not reproduced (all on an assumption) and 12 blocked, all for
missing data; the eight claims that also use an input from outside the dataset
are counted apart: one partially reproduced and four not reproduced, all on an
assumption, and three blocked for missing data. All 31 claims are on the
dandiset. The first verification round agreed with 29 of the 31 outcomes as
they stood and the second with all 31, and nothing was proposed after the
second, so there was no third round. It pins version 0.261006.1856, the only
published version; the paper cites none. The paper, Semenov, Silkuniene,
Silkunas, Pakhomova, Bixler, Ibey, Kochunov and Pakhomov, "Sub-microsecond
optical measurements of cell membrane charging and lesioning by pulsed electric
fields" in Bioelectrochemistry, images CHO cells stained with FluoVolt and
Di-8-ANEPPS by strobe microscopy during 1-us and 0.3-us pulses at 43 to 1400
V/cm, and reports the charging at the anodic and cathodic poles and its limits
(Figs. 1 to 4), its change with Gd3+ and a conductivity calibration by Eq. (2)
(Fig. 5), Fluo-4 calcium responses (Fig. 6) and membrane recovery measured with
a 150 V/cm test pulse (Fig. 7). The claims were written from the version of
record, from a PDF supplied by a person, without opening the figures; the paper
names no supplement and links no code ("Data will be made available on
request"), and the claims file follows the checked file for the same paper on
dandiset 001518, with the paired and unpaired t-test both made readings in two
claims of absence and `fig2b-di8-bleaching` added; the check made seven
corrections, among them a dataset.id copied as "001518". The claims that use
the calculated IMP need the charging time constant of reference [20] (Semenov
et al. 2025, tau = 44.5 ns per um of radius) as an outside input, and the
background method was taken from the same reference. The 16 claims on the 1-us
escalations and Eq. (2) were tested. Reproduced are `fig1-pole-dimming`,
`fig2b-di8-climbs-to-570`, `fig2b-di8-bleaching` (-5.11%, fragile, 38 of 56
five-cell subsets passing), `fig2b-di8-decline-within-set`, whose part at 780
V/cm cannot be told from bleaching, and `fig7b-charging-during-pulse` (1.465
and 2.153), which rests on matching the volts to V/cm in order, no reading
passing with the field proportional to the volts. Partial are
`fig3-dye-sensitivity` (Pearson 0.964 and 0.762 within, slopes 21.57 and 7.38
against 26 and 9.1), `fig4b-cathodic-asymmetry` (anodic 1400 V/cm value -21.6%
against -30 +- 3) and `fig5b-conductivity-calibration`, which uses no
recordings (a 10-fold rise gives 1.33% against 2 +- 0.2, a 100-fold rise 11.87%
within 12 +- 1.2). Not reproduced are `fig2a-fluovolt-saturation` (49.4 and
-69.8% against 66 and -83), `fig2a-fluovolt-stable` (both start/end readings
find changes among 24 tests, which about 70% of stable recordings would also
fail), `fig3-fluovolt-nonlinear` (Di-8-ANEPPS departs from the shared line on
the cathodic side, slopes 11.63 anodic and 3.13 cathodic),
`fig4a-fluovolt-limits` (49.3 and -72.1% against 71 +- 10 and -83.5 +- 5),
`fig4a-fluovolt-cathodic-decline` (49.3% at 360 V/cm against 71 +- 10),
`fig4b-di8-limits` (the anodic maximum at 780 V/cm), `fig4b-first-10-pulses`
(43.1% against 66 +- 15) and `fig4c-equator-follows-cosine` (16 of 24 arcs
differ). Several of these hold only under the adopted background 8 to 10 um
out: the band 14 to 20 pixels out passes `fig2a-fluovolt-saturation`, both Fig.
3 slopes and `fig4b-first-10-pulses`, and the near band passes
`fig4b-first-10-pulses` and `fig4b-cathodic-asymmetry`. The other 15 claims are
blocked because their experiments are not in the dandiset. The author's first
run gave 5 reproduced, 3 partially, 8 not reproduced and 15 blocked. The author
asked no questions of a reader, so the reader's run and the author-answers run
changed nothing. Round 1 disagreed with two outcomes and found that the volts
were matched to V/cm in order without running a field proportional to the
volts, that the Fig. 3 slopes pass only with a pixel giving the paper's 8-um
radius, that the background distance was not swept, that bleaching may account
for the decline at 780 V/cm, that the criterion of `fig2a-fluovolt-stable` has
a family-wise false-positive rate near 70%, and that subset shares, the
equal-area radius and per-pole backgrounds were missing; in reply
`fig2a-fluovolt-saturation` moved to not reproduced and `fig3-dye-sensitivity`
to partially reproduced, a dump of one file showed no pixel size, the outline
overlays it asked for showed FluoVolt c2 at 300 V traced on a neighbouring cell
and Di-8-ANEPPS c7 at 300 and 350 V on a body inside the cell, which were
traced again (the far anodic 1400 V/cm value moving from -18.5 to -21.6%, no
outcome changing), the background sweep, the proportional-volts and 8-um pixel
variants and a bleaching control were added, and a reader was asked in
`questions/001517.yaml` whether the `fig2a-fluovolt-stable` criterion should
correct for its 24 tests. Round 2 agreed with all 31, found every assumption
stated and reasonable with qualifications on the volts mapping, the pixel size
and the background distance, noted that the c7, c10, c12, c13 and c14 outlines
are wavy and cut inside the membrane, and found sentences the outputs did not
support (three re-traced sets listed as two, the anodic pole said not to grow
beyond 570 V/cm where it grows by 2.4 points, the Eq. (2) curve said to lie far
below the paper's 10-fold value where it lies about 0.7 point above, a cathodic
deficit put down to bleaching with no output removing those points, a radius
range of 7.7 to 14.6 um no output printed, and README rows without their
qualifications), all corrected; side fits without the 43 V/cm sets showed the
bleaching points explain only part of the asymmetry (cathodic slope 3.13 to
4.59, anodic 11.63 to 10.15), and an outline on the outer membrane changed none
of the four affected claims. The author's run took about 55 minutes (20:44 to
about 21:38 UTC) and nothing failed; the notebook ran in about 5.6 minutes at
first, 538 s after the author-answers run, 374 s after round 1 and 821 s at the
end. Untracked dotfiles, `.idea`, `.vscode`, `.mcp.json` and a `scripts` folder
at the repository root, which the author did not create, were left alone.

The dandiset holds only the 1-us escalation strobe images, 220 sets of 40
baseline and 60 pulse images from 6 FluoVolt and 13 Di-8-ANEPPS cells; the
alternating 150/230 V/cm sets of Fig. 2C/D, the 0.3-us pulses of Fig. 4D, the
Gd3+ cells and controls of Fig. 5A, the Ca2+ imaging of Fig. 6 and the
two-pulse experiments of Fig. 7 are not in it, so 15 of the 31 claims cannot be
tested. Dandiset 001518 also names the paper and is by its title a FluoVolt and
Di-8-ANEPPS comparison; it is a separate target and its files were not read.
The pulse amplitude is given only as generator volts in a free-text session
description (25 to 350 V), while the paper reports field strengths from
Sim4Life modelling (43 to 1400 V/cm) that are not proportional to the volts,
and no field gives the conversion; the nine steps were matched in order, which
the first step supports (from 25 to 50 V the response triples, 3.05 for
FluoVolt and 2.90 for Di-8-ANEPPS, against 3.49 for the paper's steps and 2.00
for proportional volts). The files hold raw images only, one ImageSeries each
with no ImagingPlane, Device, field of view or grid spacing, so the pixel size,
the field direction, the cell outline or ROIs and which frames carry the pulse
are not stored (the 40/60 split stated in the paper is consistent with the
data); with 0.267 um pixels the cells have mean radii of 7.8 to 15.1 um,
larger than the 8 um the paper gives as typical, and the Fig. 3 slopes come
out 21.6 and 7.4% per 100 mV, where 0.192 um gives 26.6 and 9.5 as in the
paper. The paper gives no background distance for the strobe images, and a
background 2 to 4 um out, 8 to 10 um out or none changes the pole dF by up to a
factor of three (FluoVolt cathodic at 360 V/cm 78.5, 49.4 and 23.7%). Every
session description gives an electrode distance of 1.00 mm where the paper and
its reference [20] give 1.6 mm, and the dandiset description says Di-8-ANEPPS
was used, replacing FluoVolt, while 68 of the 220 sets (6 cells) are stated to
be FluoVolt. Frame 0 of 137 of 141 sets examined and 290 further frames hold no
laser flash and are not flagged; apart from frame 0 they are five times as
frequent among pulse frames (257 of 8460) as among baseline frames (33 of
5499), and averaging them in moves the Di-8-ANEPPS 43 V/cm offset from -5.1 to
-2.2%. The dandiset has eight Di-8-ANEPPS cells with the nine-step escalation
where Fig. 2B and 4B report n = 5, five FluoVolt cells with it (one with an
extra 350 V set first) and a sixth with a finer escalation where Fig. 2A and 4A
report n = 4, and five Di-8-ANEPPS cells recorded on 2025-01-22 on other steps
the paper does not describe, with no statement of which cells the paper used.
Of the paper itself, Results 3.5 says a 10-fold rise of the effective membrane
conductivity reduces IMP by about 2%, where Eq. (2) with the constants of
Methods 2.3 gives 1.3% (a 2% reduction needs a 15-fold rise); the 100-fold
value (12%) agrees with the equation. Questions are put to the paper's authors:
where the background ROIs were placed; the pixel size and how the radius was
measured; which generator amplitude corresponds to each field strength; and
which cells form the n = 4 FluoVolt and n = 5 Di-8-ANEPPS groups.

The author's points on the protocol: it does not cover choosing among readings
when the support comes from the data and not the paper, so the background 8 to
10 um out was adopted as an assumption with all three readings shown; it does
not say how an open detail that crosses each criterion's own readings combines
with them, so each criterion was applied within the adopted background; the
absence rule ignores multiple comparisons, so `fig2a-fluovolt-stable` was
recorded as not reproduced with the chance rate noted; nothing covers an
unnamed subset of cells, so all 8 were used and all 56 subsets reported;
`elsewhere` does not cover a sibling dandiset in the same archive, so
`data_missing` was kept and 001518 not read; the clock-check guidance assumes
trial tables or spikes, so the 40/60 split was tested by moving the split
frame; the line between partially and not reproduced is unclear when value
conditions fail but the shape holds; and taking a fitted constant from a cited
paper is not clearly covered by `inputs` or entry `related`, so it was recorded
under `inputs` with its DOI.
