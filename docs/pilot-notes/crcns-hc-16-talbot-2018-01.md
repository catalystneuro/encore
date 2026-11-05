# crcns-hc-16, Talbot et al. 2018

One claim reproduced (on an assumption), seven partially (one on an
assumption), ten not reproduced and fourteen blocked, all fourteen for missing
data. The first verification round agreed with 29 of the 32 outcomes as they
stood and the second with all 32; nothing was proposed after the second, so
there was no third round. CRCNS does not version data sets, so the version is
recorded as unversioned with the data set's DOI (10.6080/K01V5C44) and the
zip's MD5 from `checksums.md5`. The paper, Talbot, Sparks, Dvorak, Curran,
Alarcon and Fenton, "Normal CA1 Place Fields but Discoordinated Network
Discharge in a Fmr1-Null Mouse Model of Fragile X Syndrome" in Neuron, records
fEPSPs in CA1 slices and, in vivo, CA1 tetrode units of 12 WT and 9 Fmr1-null
mice in a small and a large box, a ring and a stationary or rotating arena,
and finds place fields alike in the two genotypes but the coordination of
discharge across cells altered; the data set holds 41 sessions from 15 of the
21 mice, with spike times and positions in TS files from the large box and the
stationary and rotating arena. The claims were written from the PyMuPDF text
of the version of record and its supplement, without rendering any figure,
and from three FentonLab repositories the paper links (SpikeField,
CorrelateBPFSpikeTrainEpisodes and PositionalInfo). The single-cell, spatial,
overdispersion, covariance, Kendall, locomotion and rotating-arena claims
could be tested; the slice, LFP phase, remapping and avoidance claims and the
unit counts could not. Reproduced is `locomotion-similar` (genotype p = 0.63,
interaction p = 0.67 over 34 recordings), resting on pooling the large box and
stationary arena, as within each environment the interaction is significant
in opposite directions (large box p = 0.021, stationary arena p = 0.0076).
Partial are `interneuron-proportion` (33.5% WT and 44.5% Fmr1-null in R1, far
outside 12.4 and 29.3), `figs3-nonspatial-properties-similar` (a rate effect,
p = 0.0042), `tables1-place-cell-properties-similar` (place cells alike,
interneuron rates 5.40 and 10.34 AP/s, p = 0.0105), both fig4b covariance
claims (r = 0.061 against 0.021, p = 0.023, at 30 passes),
`fig5b-frame-specific-ipos` (p = 0.012 in reading B, 0.13 without M37, 0.25
in reading A) and `figs6-room-frame-preference`, which rests on reading B and
would not be reproduced under reading A (p = 0.067). Not reproduced are
`place-cell-proportion` (23.6% and 21.4% against 47.8% and 42.2%),
`fig2-spatial-quality-similar`, `tables1-nonspatial-active-pixels`, both
overdispersion claims, the four Kendall and network claims and
`fig5c-ensemble-coordination`. Every tested outcome rests on using every
sorted cluster except cluster 0 in place of the paper's well-isolated cells,
and most on a spatial scale assumed from the tracked extent and the enclosure
sizes. The author's first run had 2 reproduced, 5 partially, 12 not
reproduced and 13 blocked. The author asked no questions of a reader, so the
answer and author-answers runs changed nothing. Round 1 disagreed on
`unit-and-cell-counts`, which it found blocked as the data set is a subset,
on `interneuron-proportion` and on `fig5b-frame-specific-ipos`, gave
metadata insufficient as the block reason of `figs4-remapping-similar`, and
found that the literal pass rule passes almost every interval, that no
isolation proxy or scale-free variant was run and that the Ipos visit minimum
was counted per interval; in reply the three outcomes changed, the count
reading of the pass rule was run as a variant and the rule went to a reader in
`questions/crcns-hc-16.yaml`, a refractory filter (70 of 774 clusters removed)
and the code's 32 x 32 grid (45 clusters change class) were added, and
`locomotion-similar` was marked assumed. Round 2 accepted data missing for
figs4, noting that the claims file misreads Table S2, asked that figs6 say its
assumption settles a question fig5b leaves open, and found sentences the
outputs did not support, among them that clusters mixing many units do not
explain the interneuron excess; in reply the text was corrected, the two
variants were run on the pass and Kendall claims, a single-permutation check
showed the p = 0.0004 shuffle to be the most extreme of 100, and two more
points went to a reader, the claims file's reading of Table S2 and
`fig4b-covariance-40-passes` meeting its criterion under the count rule on the
grid together (0.182 against 0.056, p = 0.0004). The round-2 report's own
summary counts 8 partially and 9 not reproduced where the record has 7 and 10.
The author's run took about 30 minutes (04:09 to about 04:39 UTC); nothing
failed in the final run, though one editing step dropped the place-cell
section, which was restored. The notebook ran in about 80 s at first, 70 s
after the author-answers run, 79 s after round 1 and 140 s at the end.

The data set holds part of the paper's data: 8 of 12 WT and 7 of 9 Fmr1-null
mice, the large box and the stationary and rotating arena, but no small box or
ring sessions, no sleep or quiet-wakefulness recordings, no LFP, no slice
recordings and no avoidance sessions, so fourteen of the 32 claims cannot be
tested. No isolation measures (IsoIBG, IsoINN), waveforms or cell classes are
given, and the files hold every sorted cluster, including cluster 0, so the
paper's 226 WT and 334 Fmr1-null well-isolated cells cannot be selected; Table
S2 lists fewer cells per session than the files hold clusters (15 against 50
for M16 in stationary arena 1). Positions are in tracker pixels (0 to 255) with
no spatial scale, and the tracked extent of the large box is about 186 pixels
in most sessions, about 218 in three (M9, M10, M11) and 188 x 207 in M1. The
header's SAMPLING_INTERVAL and FIRST_TIMESTAMP do not give the times of the
position samples: spikes lie up to 118 samples (about 4 s) after the nominal
time of the sample they are filed under, and the data descriptor's example
header gives 58.3 samples/s where every file has 30.0. Six spike trains have
one backward step in their spike times, of 0.2 to 1.4 s. Nothing identifies a
cell across sessions; sessions of a day mostly share a cut file, but M29
stationary arena 1 and M34 stationary arena 2 have their own, and box and arena
sessions are on different days with different cut files. The _0-15min and
_15-30min files repeat the full-session files except one position sample at
the split, so a spike filed under it is lost (one of five spike trains
checked). Questions are put to the paper's authors: which recording classifies
a cell as a place cell, interneuron or non-spatial cell, and for the
rotating-arena cells of Figures 5 and S6 whether that is the same-day
stationary session or the rotating one; and which recordings enter the
locomotion test of Figure S5B and whether environments are pooled.

The author's points on the protocol: it does not say what to do when the
paper's cell selection cannot be applied, so every claim was tested on all
sorted clusters with the gap recorded as a deviation; partially reproduced is
not defined for claims of absence over several measures, so it was used when
some measures held and others did not; `measured` has no way to say a value
cannot be measured, so the nearest cluster counts were given with an
explanation; the clock check is written for spikes against trial tables, so
spikes were shifted against positions and spatial information compared (the
true alignment highest in 29 of 34 sessions); and the handover removes Result
cells, so the two fig4b claims that share a code cell share one Result cell.
