# martinez-conde-2019, Martinez-Conde et al. 2019

Nine claims reproduced, two partially, five not reproduced and two blocked
on the data set, plus one claim needing an outside input, blocked; both
verification rounds agreed with all 19 outcomes and nothing was proposed, so
there was no third round. CRCNS does not version data sets, so the version is
recorded as unversioned with the DOI (10.6080/K05D8Q1T), and the notebook
checks the zip's ETag against its MD5 in `checksums.md5`. The paper,
Martinez-Conde, McCamy, Troncoso, Otero-Millan and Macknik in PLoS ONE
(14(3) e0210941), records V1 single units in two rhesus monkeys viewing
Vasarely-based illusory corner-folds and reports that the response at the
fold midpoint grows as the corner sharpens (S40 > S52 > S90 > P180), that the
relation to corner angle is not linear, and that sharper corners give
responses equivalent to higher contrasts along a straight Edge. The claims
were written from the version of record (PMC6438452) without the
supplementary tables or the reference list, and the paper links no code. The
data set holds the authors' spike rate maps made at 60 ms, not the
recordings, so `spikes-per-condition` and the latency analysis of S3 Fig are
blocked as `data_missing`, as is `fig7d-dog-similar`, which needs the output
of the difference-of-Gaussians model of reference [3]. Reproduced are the
responses above baseline of Fig 4A, the pairwise tests of Fig 4B (S40
against P180 p = 2.1e-06),
the average maps, `fig6-midpoint-representative`,
`fig7c-fold-edge-significance`, `fig7d-nonlinear` and the Table 1 rows for
the Edge, S52 and S40; `fig4b-spike-rate-difference` is partial, as S90 is
8.39 spikes/s, 2.30 below 10.69 and outside its 1.94, and so is
`table1-p180` (four of five values). Not reproduced are `neuron-counts` (53
neurons in the files against 58), `s4-baseline-no-difference`
(Kruskal-Wallis p = 0.025 under the main reading), `table1-s90`,
`fig7a-rms-contrast-fit`, where neither reading of RMS contrast rises from
0.61 to 0.943 and a contrast saturating near 0.95 would need a display black
level the paper does not give, and `fig7c-fold-edge-equivalence`, which is
borderline: under reading (b) S40 is nearest the 94.3 level, 4.3 from 90
against a step of 3.7, and counting one step as one level would pass. Most
outcomes rest on an assumption about where the baseline squares lie, which
the Methods leave open: per stimulus, the placement whose values come closest
to the files' own BaseActivity (centred on the corners for Square and Edge,
inside them for the Star), and the bottom corners of the ROI for Corners;
s4, table1-s52 and table1-s90 change with the placement and with which
neurons are included. Before verification two questions went to a reader, on
which Corners fold the S40 claims use, and the claims file was amended to
take the bright fold alone, which changed no outcome. In the first revision
the author found that the Square and Edge baseline squares had been read as
zeros outside the authors' 151 DU frame; corrected, `table1-p180` moved from
not reproduced to partially reproduced, `table1-s90` from reproduced to not
reproduced and `table1-s52` from partially reproduced to reproduced, and a
bug in `register_shift` that had left three Corners files unchecked was
fixed. Round 2 found three statements with no printed output behind them,
among them `smoothed_image_norm` missing from 35 of 77 files where the field
table gives 39, and these were corrected. The notebook runs in about 6 min
with 1.1 GB peak memory and nothing failed; one cleanup, removing an empty
`.claude/` directory inside the entry, was refused.

The data set holds 53 neurons, not the 58 the paper analysed: the
spreadsheet V1_Vasarely_data_SMC.xlsx lists 58 cells, but five have no
condition marked and no files, and per condition the files hold 22 Square
and Edge, 27 Star and 26 Corners recordings, against the paper's 25, 30 and
28. No file holds spike times, eye positions or spike count maps, and only
one (ABC050900J1A) holds an eye time map. The maps are in gaze coordinates,
and no file gives the receptive-field offset that places them on the
stimulus; the authors' aligned maps, in an undocumented Standard struct, are
present for all Corners and Square and Edge files but only 12 of 27 Star
files, so 15 Star recordings cannot be analysed, and the offset differs
between conditions of the same neuron by up to about 50 DU, so it cannot be
carried across. Standard also holds BaseActivity in 38 of 60 files, with no
description of how it was computed, and it matches no placement of the
baseline squares exactly. The data descriptor is wrong about the fields:
`image` is the spike rate per 1 ms eye-time sample, not raw spike counts,
and `smoothed_image_norm` is absent from 39 of 77 files, while in the 38 that
hold it it is smoothed_image minus BaseActivity in 5, a linear rescaling in
21, not a linear function of it in 11 and non-finite in 1. Two files in the
Star folder, ABS042700J2 and ABS051000J3, are recordings with a Corners-type
stimulus, and the spreadsheet marks both cells as tested with the Star. In
four Square and Edge files the 100% end of the Edge lies beyond the screen
border, where the Methods say the rectangle was sometimes partly off the
display "but never its edge", and the Edge values come from the other 18.
Two questions are put to the paper's authors, where the baseline squares lie
and how BaseActivity was computed, and how the RMS contrast of Fig 7A was
defined. The paper's sizes also disagree: the Star ROI is given as 160 x 160
DU while the authors' Star frame in the files is 321 x 321 DU, and the
circumscribing square of the Square as 8.84 DVA and as 138 DU, where 8.84
DVA is 141.4 DU.

The author's points on the protocol: step 2's check that the data share the
clock of the trial tables does not fit spatial maps with no time base, and a
spatial contrast across the Edge was used; the protocol assumes data close to
the recordings, while these are the authors' processed maps; the rule that a
claim is reproduced if any of the criterion's readings matches and the rule
that readings of an open method detail must agree sit side by side, and the
first was applied to the criterion's readings and the second to the baseline
placement; a claim of absence is to be judged on "the paper's test", which
the paper does not name; `measured` has no rule when no reading matches, and
the main reading was recorded; it is not clear whether a claims-file reading
that does not fit the data's geometry counts as a misreading, and a reader
was asked; and "pinned published version" does not map onto unversioned
CRCNS, for which the ETag-to-MD5 check was used.
