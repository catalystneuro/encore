# crcns-ret-1, Lefebvre et al. 2008

Three claims reproduced, two not reproduced and twenty-one blocked on the
data set, none partially reproduced. The data set is on CRCNS and has no
versions, so it is recorded as unversioned; the notebook checks the zip's MD5
against `checksums.md5` and lists each member's CRC-32. The author put one
question to a reader, which flickering-bar recording of a retina to use; the
paper does not say, so the claims file now names three readings (A, the first
vertical-bar recording; B, all vertical-bar recordings pooled; C, the
horizontal-bar recording where the retina has one, otherwise A), which the
first run had already used, and the answer changed the text of six claims and
no outcome. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with all 26, and asked for
the frame and onset search of 20080702_R4 to be run in the notebook. The search
showed that the stated frame lengths of two vertical-bar recordings are wrong,
and with the corrected frame the DKW bands overlap under reading B with the svd
separation, so `fig9d-rf-size-similar` separates in 17 of 18 combinations and
moved from not reproduced to blocked as `methods_underspecified`. Round 2
agreed with all 26, including the change, and nothing was proposed, so there
was no third round. The paper, "Gamma-Protocadherins regulate neuronal
survival but are dispensable for circuit formation in retina" in Development,
removes the Pcdh-gamma cluster from mouse retina with Chx10-Cre or
Pax6alpha-Cre, and reports from histology that the mutant retina is properly
laminated but its INL and IPL are thinned, with increased apoptosis, that
deleting Bax rescues the neurons that die, and that their processes reach the
appropriate IPL sublaminae, and from multielectrode recordings of retinal
ganglion cells that mutant cells have a similar variety of responses, similar
receptive field sizes and an unaltered threshold, with a slower time course, a
lower firing rate and a reduced gain. The 15 histology claims and the four on
flashing spots, flashes, moving bars and gratings are blocked as
`data_missing`; the cell counts and the six claims on the white-noise responses
were tested. `fig9-cell-counts` is not reproduced (200 mutant and 122 control
units against 115 and 143), and `fig9g-threshold-unaltered` is not reproduced
(36 of 36 combinations separate, with mutant thresholds higher).
`fig9e-slower-time-course` (36 of 36, mutant medians longer by 16.7 to 33.3
ms) and `fig9f-lower-firing-rate` (9 of 9, reading A median 3.82 against 9.02
Hz) are reproduced, and `fig9h-gain-reduced` is blocked as
`methods_underspecified` because the printed and continuous forms of the
nonlinearity disagree. `s3-receptive-field-surrounds` is reproduced under its
criterion, but null STAs meet the rule in 194 to 198 of 200 mutant and 119 to
121 of 122 control units, so the result is no evidence for or against
surrounds. Some outcomes rest on weak ground: fig9d rests on one borderline
combination and on the frame correction, and with the frames as deposited all
18 separate; among units with an STA peak above twice the null's (103 mutant,
107 control), fig9f and fig9g would be blocked, as no DKW band separates, so
their outcomes hold only on all units, as the claims file's header reads the
groups; and in fig9-cell-counts a threshold of STA strength between 1.5 and 2
could put the mutant count inside its tolerance, so the outcome rests on the
control count, which no reading can bring inside.

The data set holds only the white-noise recordings behind Figure 9D to 9H. The
histology of Figures 1 to 8 and Supplementary Figure 1, and the flashing-spot,
flash, moving-bar and grating recordings of Figure 9A to 9C, are not in it, and
the paper names no other deposit, so 19 of the 26 claims cannot be tested. It
holds 200 mutant and 122 control units (and 3 from a Bax -/- mutant), where the
paper's Figure 9 has 115 mutant and 143 control cells, and it does not say how
its units relate to the paper's, which were kept, or why the counts differ. 95
of the 122 control units are labelled "WT (chx10 het)", while the paper's
Figure 9 legend gives the controls as Pax6-Cre;Pcdh-gamma +/f-del or
Pcdh-gamma f-del/f-del without Cre. In the 8 recordings of 20080628_R4,
20080628_R6, 20080702_R1 and 20080702_R4, 82 of 86 spike trains are not in time
order: each runs to 1440 s and then holds a second segment between 720 and 780
s, though the stimulus runs to 1500 s, which is consistent with the last minute
stored with a 720 s offset in place of 1440 s. The frame lengths stated for the
vertical-bar recordings of 20080702_R1 and 20080702_R4 (16.6691 and 16.6653 ms)
are not those of the stimulus; rebuilt with the stated frame, the bars of
20080702_R4 give no STA above the null in any of its 12 units (median ratio
0.96), and with 16.6718 ms, the frame of every other bar recording, the median
ratio is 2.57 and 10 of the 12 units have peaks above twice the null's. 16
pairs of units share 70 to 100% of their spikes within 0.5 ms in every
recording of their retina (12 pairs in mutant retinas, 4 in a control retina),
most likely single neurons sorted twice, and the data set does not mark them.
The files do not give the age of the mice, the Pcdh-gamma allele (the paper's
Results say fcon3 and its Figure 9 legend f-del), the region recorded in the
Pax6-Cre retinas, whose periphery alone the paper used, or the cell type of the
units. Other findings: 97 of 200 mutant and 15 of 122 control units have an STA
peak less than twice the null's, and much of the fig9d difference comes from
them; all 5 retinas recorded with 8.3 um bars are mutant, and every control
retina was recorded with 16.6 um bars; and one checkerboard recording
(20080628_R5) has 1 or 2 spikes near 2 s out of order in 15 units.

The notebook ran in 277 s in the first clean run, 251 s after the answer,
about 8 minutes after round 1 and 500 s after round 2. Two string-escaping
errors in the author's notebook generator were fixed along the way. Round 1's
points led to a label-shuffle calibration of the bands (the binomial band
separates in 35% of shuffles, the bootstrap band in 37% and DKW in 0 of 1600),
counts of LN fits at the grid edge, a synthetic check of the LN fit, a table of
units per retina and example STAs; with the corrected frame the mutant count
above an STA ratio of 1.5 went from 126 to 138. Round 2 found statements the
outputs did not support, among them the README stating the misplaced last
minute as fact, a summary sentence saying the results hold with the 16.6 um
bars alone, which is false for fig9d, and grid-edge counts described as fits
at the top of the grid where both ends were counted, and these were corrected;
the author then added every claim's combinations under all three readings for
the frames as deposited, units with clear STAs and the 16.6 um bars alone.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: "units with a flicker
response" in fig9-cell-counts is undefined; the protocol says how to count
recordings deposited twice but not units sorted twice; the criteria do not say
what to do when bands separate in both directions; a criterion can be met by
noise, with no rule for when its own null meets it; the clock check assumes
trial tables, which continuous white noise does not have; the schema has no
kind for disagreement between the paper and the data set's labels; and
`archives.md` asks for MD5s of the files read, where only the zip has one.
