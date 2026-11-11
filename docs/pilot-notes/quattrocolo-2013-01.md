# crcns-hc-9, Quattrocolo et al. 2013

One claim reproduced (on an assumption), none partially, none not reproduced
and 25 blocked, all 25 for missing data. The first verification round agreed
with all 26 outcomes and the second with all 26; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned and pinned by the MD5 of the zip, which
matches `checksums.md5`. The paper, Quattrocolo and Maccaferri, "Novel
GABAergic Circuits Mediating Excitation/Inhibition of Cajal-Retzius Cells in
the Developing Hippocampus" in the Journal of Neuroscience, records
Cajal-Retzius cells and their GABAergic inputs in acute hippocampal slices of
CXCR4-EGFP and Sst-IRES-Cre;ChR2(H134R)-EYFP mice aged P10 to P19, with paired
recordings, optogenetic stimulation of O-LM cells, cell-attached recordings and
dynamic clamp; the data set holds one zip of three ATF files, one per O-LM cell
of Figure 7, each with 15 one-second current steps recorded at 20 kHz. The
claims were written from the extracted text of the version of record, which
printed the signs =, < and > as a replacement character, as the PDF could not
be rendered; the paper has no supplement and links no code. The check made 12
changes and left two points open, the unread signs and the inferred paragraph
numbers. Only the O-LM sag of Figure 7A and 7D could be tested, and none of the
Cajal-Retzius claims could. `fig7a-olm-sag` is reproduced on the claims file's
measure, which the paper does not define: on the -100 pA step reading (a) gives
sags of 17.5, 7.9 and 8.7 mV and reading (b) sag ratios of 0.448, 0.224 and
0.208, above 0.1, so 3 of 3 cells under both. Reading (a)'s threshold of twice
the pre-step SD is also passed by each cell's 0 pA sweep (2.8 to 20.1 pre-step
SDs), as the 75 ms baseline misses slow fluctuations over the 1 s step, so the
outcome rests on reading (b) and on the -100 pA sags being 4.5 to 7.3 times the
0 pA value. The author's first run gave the same outcomes, with V_min taken as
the raw minimum (17.6, 8.0 and 8.8 mV; ratios 0.449, 0.225 and 0.210). The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 found that the raw minimum biases reading (a) toward a
sag (4.0 baseline SD on a synthetic trace without sag, 0.7 with a 1 ms running
mean), that the mapping of files to Figure 7 panels comes from the superseded
description, and that it could not compare the traces with the printed figure
or measure the noise floor on the 0 pA sweeps; in reply V_min was taken from a
1 ms running mean, a cell was added that runs the measure on the 0 pA sweeps and
100 synthetic traces, which found the weakness of reading (a) above, a zoomed
plot of the first 300 ms of each -100 pA step was added but not set against
Figure 7, as `pdftoppm` is not installed, and a sentence that put the 7D cell's
ratio between those of the 7A cells was corrected. Round 2 found sentences the
outputs did not support (the variant minima attributed to the raw V_min, a
Summary saying reading (b) separates sag from noise in these recordings, and a
README run time no output showed); in reply the text was corrected, the 0 pA
"sag" was shown as 0.038 to 0.061 of each cell's -100 pA hyperpolarization, and
a cell printing the run time was added. The author's run took about 10 minutes;
a stray quote in a YAML scalar and bold labels in the notebook were fixed. The
notebook ran in 13 to 14 s at first, 14 s after the author-answers run and about
10 s after each round. The untracked files in the repository root were left
alone.

The data set holds only the current-step recordings of the three O-LM cells of
Figure 7: none of the Cajal-Retzius recordings behind Figures 1 to 6 and 8 to
12 are in it, nor the light-evoked responses of Figure 7C and 7D, and the paper
gives no data availability statement and names no other archive; the data
set's title and description say it holds only the O-LM firing patterns. The
description gives the steps as -100:30:+250 pA, where all three files hold 15
steps from -100 to +250 pA in 25 pA increments, and says the injection starts
about half a second into the sweep, where it starts at 75 ms and ends at 1.075
s. The current description (version 0.7) gives no animal, age, mouse line or
Figure 7 panel for each cell; the superseded description under hc-9/old/ does
(1May2012_P3 P13 and 20Sept2011_P2 P14, CXCR4-EGFP; 24October2012_C2 P15,
Sst-IRES-Cre;ChR2(H134R)-EYFP), matching the Figure 7 legends, and calls the
files ABF, though they are ATF text files. A question is put to the paper's
authors: whether the sag of Figure 7A and 7D was judged by eye or by a measure
such as the sag ratio.

The author's points on the protocol: it does not say whether superseded
documentation in an archive (CRCNS `old/`) is the dataset's metadata or outside
data, so it was treated as the dataset's own documentation and stated in a
deviation; step 1.6 raises a question for the paper's authors "in either case",
so `assumed: true` was set and a `methods_unavailable` question added though
both readings agreed; step 2's clock check is written for spikes with trial
tables or continuous sessions and does not fit current-clamp sweeps, so the
delay from the current step to the voltage response was measured and the step
window compared with a shifted one; and the claims file's header says 27 claims
in places where there are 26.
