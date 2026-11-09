# 001525, Semenov et al. 2026

Two claims reproduced (both on an assumption), three partially (two on an
assumption), none not reproduced and 11 blocked, all for missing data; the 11
claims that also use an input from outside the dataset are counted apart and are
all blocked for missing data. All 27 claims are on the dandiset. The first
verification round agreed with 26 of the 27 outcomes as they stood and the
second with all 27, and nothing was proposed after the second, so there was no
third round. It pins version 0.261006.1856, the only published version; the
paper cites none. The paper, Semenov, Silkuniene, Silkunas, Pakhomova, Bixler,
Ibey, Kochunov and Pakhomov, "Sub-microsecond optical measurements of cell
membrane charging and lesioning by pulsed electric fields" in
Bioelectrochemistry, images CHO-K1 cells stained with FluoVolt or Di-8-ANEPPS by
laser flashes at 900 ns into 1-us pulses (275 ns into 0.3-us pulses), and
reports the charging at the anodic and cathodic poles as the field is raised
(Figs. 1 to 4), its change with Gd3+ and a conductivity calibration by Eq. (2)
(Fig. 5), Fluo-4 calcium responses (Fig. 6) and membrane recovery measured with
a 150 V/cm test pulse 5 us after a conditioning pulse of 150 to 1400 V/cm (Fig.
7). The claims were written from the version of record, from a PDF supplied by a
person, as extracted text; no page could be rendered, and Eq. (2), garbled in
the text, was read as the thin-shell formula of Kotnik et al. The paper has no
supplement and links no code ("Data will be made available on request"), and
the claims that need the calculated IMP use the tau fit of reference [20]
(Semenov et al. 2025) as an outside input. The check made ten corrections and
left three points open, among them fig5b. The claims on the Fig. 7 test pulse
and Eq. (2) were tested. Reproduced are `fig7a-test-pulse-cosine-up-to-1000`
(no pole reading differs from the benchmark after 360 to 1000 V/cm, smallest p
0.059; hindered after 1200 and 1400 V/cm at the cathodic pole, unpaired p 0.022
and 0.0010) and `fig7b-test-pulse-unchanged-to-760` (smallest p 0.098; 79.7% of
control at 1000 V/cm at the anodic pole only, 57.5% at the cathodic). Partial
are `fig7b-test-pulse-reduced-1200-1400` (cathodic 25.2% and -11.3% of control,
significant but outside 70 +- 7 and 50 +- 5; the anodic 68.7% and 48.0% within
tolerance but p 0.086 and 0.011), `fig5b-conductivity-calibration`, which uses
no recordings (11.87% for a 100-fold rise within 12 +- 1.2, 1.33% for a 10-fold
rise outside 2 +- 0.5), and `fig7c-full-reseal-mild-residual-strong`, whose
reseal and residual parts hold while the test pulse finds a pole difference
after 1400 V/cm (paired p 0.0002) and the part during the pulse cannot be
tested. These outcomes rest on an automatic membrane trace, the rank mapping of
volts to V/cm and a single 50 V pulse as the benchmark; the Fig. 7 outcomes
hold in 19 of 22 variants, failing in the 3 with the first round's trace, so the outcome
turns on the edge trace. The other 22 claims are blocked because their
experiments are not in the dandiset. The author's first run gave 1 reproduced, 1
partially, 1 not reproduced and 24 blocked, with
`fig7b-test-pulse-unchanged-to-760` blocked as methods_underspecified because
the paired and unpaired tests disagreed. The author asked a reader which test
Fig. 7B used; the reader answered from the paper that it is the unpaired
two-sample t-test against the control group and amended three criteria, and the
author-answers run moved `fig7b-test-pulse-unchanged-to-760` to reproduced and
`fig7a-test-pulse-cosine-up-to-1000` to partially reproduced (1200 V/cm not
significant, p 0.067 to 0.19). Round 1 disagreed with one outcome, finding that
the reseal and residual parts of `fig7c-full-reseal-mild-residual-strong` need
only test-pulse data, and found that the control profile carried an
unexplained mean dF of -4.6%, that the metadata strengths and the 1.00 mm gap
contradicted the rank mapping without discussion, that the single-pulse
benchmark was stated only in a helper comment, and that no overlay showed the
analysed cell and trace, c5's cathodic dF being negative at every strength; it
had not seen the reader's amendment. In reply the overlays showed the plain
intensity peak lay a median 11.7 and 8.9 px inside the outer edge of c5 and c9,
on bright dye inside the cell, so the trace became the intensity peak within 8
px inside the outer edge (2.5 to 4.8 px inside it in every cell), which moved
`fig7a-test-pulse-cosine-up-to-1000` back to reproduced,
`fig7b-test-pulse-reduced-1200-1400` from not reproduced to partially reproduced
and `fig7c-full-reseal-mild-residual-strong` from blocked to partially
reproduced; the baseline trend, the metadata strengths, the recording order and
a field direction from the control files were added. Round 2 agreed with all 27,
found the 8 px window untested, a notch in the c5 trace, that dropping c5 makes
`fig7b-test-pulse-unchanged-to-760` fail, that Results 3.7 omits a negative
cathodic dF at 1400 V/cm so that only the anodic reading can carry the paper's
~50%, and sentences the outputs did not support (54 files where 56 are printed,
a dark-frame shift of 1.3 points that holds only without a background,
bleaching said to account for the offset in size, the cathodic values said to
fall below the paper's at 1400 V/cm, a paired-test sentence leaving out the
mean of poles, and a README row leaving out the failed pole-difference part),
all corrected. In reply windows of 4 to 12 px were run
(`fig7a-test-pulse-cosine-up-to-1000` holds under every window, `fig7b-test-pulse-unchanged-to-760` and the reseal and residual
parts fail at 4 px), the c5 notch was placed 22 to 35 degrees from the cathodic
pole in its first file but within the cathodic arc in its 760 and 1000 V/cm
files, and two questions were filed for a reader, on the anodic reading of
`fig7b-test-pulse-reduced-1200-1400`, under which it would be not reproduced,
and on leaving out 1400 V/cm in the fig7c pole comparison. No run had a PDF
renderer, so Eq. (2) was checked against the PDF's text layer only. The
author's run took about 32 minutes (22:23 to 22:55 UTC) and nothing failed; the
notebook ran in 247 s at first, 205 s after the author-answers run, about 3
minutes after round 1 and 261 s at the end. Untracked files at the repository
root, which the author did not create, were left alone.

The dandiset holds only the two-pulse Di-8-ANEPPS experiment of Fig. 7A and the
bottom panel of Fig. 7B, 73 files from 10 cells; the FluoVolt, single-pulse
escalation, 0.3-us, Gd3+ and Fluo-4 calcium experiments behind Figs. 1 to 6 and
the top panel of Fig. 7B are not in it, so 22 of the paper's 27 claims cannot be
tested and one only in part. Dandiset 001526, which names the same paper and may
hold the Fig. 2C-D data, is a separate target and was not used. Pulses are
given in generator volts (50 to 350 V), not in the field strengths the paper
reports and computes with Sim4Life, and no mapping is given, so the volts were
matched to the Fig. 7A labels by rank; the paper's benchmark, a 150 V/cm test
pulse after an identical conditioning pulse, has no pair in the files, only a
single 50 V pulse, and three cells (c4, c5, c6) have two single-pulse files. Six
cells (c5 to c10) have the paper's 5-us interval where Fig. 7 reports n = 5,
with nothing saying which five were used, and four more (c1 to c4) have a 1-us
interval the paper does not report. Every file gives the electrode distance as
1.00 mm where the paper gives 1.6 mm, and the general description shared by
every file lists field strengths of 0.15, 0.52, 0.9, 1.27 and 1.57 kV/cm,
single pulses at each and intervals of 1, 5, 25 and 125 us, while the files hold
single pulses only at 50 V, six conditioning amplitudes (100 to 350 V) and
intervals of 1 and 5 us only. The files give no pixel size, no field direction
in image coordinates and no position of the analysed cell in fields of several
cells; the field direction can be recovered from the polarization (per-file
phases within 6.8 degrees sd). The image series description says exposures
began 1 us after the start of recording, while the images show the pulse from
image 40, as Methods 2.3 describe (best split at image 40 in 43 of 73 files, at
39 to 41 in 56). 70 of 73 files have a dark first image (field mean about 209
counts against 276) and 22 more dark images fall elsewhere, images with no laser
flash that nothing marks; keeping or dropping them shifts the profile mean dF at
the control by 2.17 percentage points under the background-subtracted reading.
Whether the paper subtracted a background and kept these images is put to its
authors: background removal doubles the dF scale here (5.6% to 12.6% at
150/150), and only the background-subtracted scale matches the paper's. The
images fade through each set, the membrane trace falling by about 0.10% per
image over the baseline in 43 of 44 files of the 5-us cells, which would predict
a uniform dF of -5.16% where the profiles' mean is -3.67% (r 0.18 over files);
the sign is that of the bleaching the paper reports, the size is not, and the
offset's source is not established. Of the paper itself, Eq. (2) with the
constants of Methods 2.3 gives a 1.33% IMP reduction for a 10-fold rise in
membrane conductivity where the Results state about 2%, and the 100-fold value
(11.87%) matches the stated 12%.

The author's points on the protocol: it does not say whether a sibling dandiset
the paper never names counts as deposited elsewhere, so the claims that 001526
may cover were blocked as data_missing with 001526 named in their notes; it
gives no rule when the dataset has more cells than the paper's n and the extra
one cannot be identified, so all cells were used with every leave-one-out
subset shown; the rule that a claim depending on a blocked claim is blocked also
blocked fig7c-full-reseal, although its test-pulse parts are testable; a
criterion can call a claim methods_underspecified when readings disagree even
when the paper holds evidence for one reading, and the only path is asking a
reader; `measured` is not defined for a claim with no matching reading, so the
first pole reading the criterion lists was recorded; and the `data` field fits
poorly for a claim with no recorded data, such as fig5b, so the default was
left.
